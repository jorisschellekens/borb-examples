import typing
import re
from pathlib import Path

#
# IMAGES
#

def _is_image_decl(s: str) -> bool:
    return re.compile("!\[.*\]\(.*\)").match(s) is not None


def _get_description_of_image_decl(s: str) -> str:
    m: re.Match = re.compile("!\[(.*)\]\((.*)\)").match(s)
    if m is None:
        return ""
    return m.group(1)


def _get_link_of_image_decl(s: str) -> str:
    m: re.Match = re.compile("!\[(.*)\]\((.*)\)").match(s)
    if m is None:
        return ""
    return m.group(2)


def _update_image_decl(root:Path, ls: typing.List[str]) -> typing.List[str]:
    ls_out: typing.List[str] = []
    for l in ls:
        if _is_image_decl(l):
            d: str = _get_description_of_image_decl(l)
            p: str = _get_link_of_image_decl(l)
            out_url: str = "https://raw.githubusercontent.com/jorisschellekens/borb-examples/master/"
            out_url += str(root.parent)
            out_url += "/"
            out_url += p
            ls_out.append("![%s](%s)" % (d, out_url))
            if l.endswith('\n'):
                ls_out[-1] += '\n'
        else:
            ls_out.append(l)
    return ls_out

#
# PYTHON CODE SNIPPETS
#

def _update_python_insert_decls(root: Path, ls: typing.List[str]) -> typing.List[str]:
    ls_out: typing.List[str] = []
    i: int = 0
    while i < len(ls):

        # check for code block injection markers
        if ls[i].startswith("```python") and ls[i + 1].startswith("#!"):

            # find end of block
            j: int = i + 1
            while j < len(ls) and not ls[j].startswith("```"):
                j += 1

            # update
            path_to_code: Path = Path(root).parent / ls[i + 1][2:-1]
            if not path_to_code.name.endswith('.py'):
                path_to_code = path_to_code.parent / (path_to_code.name + '.py')
            ls_out.append("```python\n")
            ls_out.append("#!" + str(path_to_code) + '\n')

            # insert code from file
            with open(path_to_code, "r") as nfh:
                ls_out.extend(nfh.readlines())

            # update
            ls_out.append("```\n")

            # update i
            i = j + 1

            # move to next iteration
            continue

        # continue
        ls_out.append(ls[i])
        i += 1

    # return
    return ls_out

#
# MAIN
#

def concat_all_readmes():
    separate_readmes: typing.List[str] = ["chapter_001/README.md",
                                          "chapter_002/README.md",
                                          "chapter_003/README.md",
                                          "chapter_004/README.md",
                                          "chapter_005/README.md",
                                          "chapter_006/README.md",
                                          "chapter_007/README.md",
                                          "chapter_008/README.md",
                                          "chapter_009/README.md"
                                          ]
    
    lines_concat: typing.List[str] = []
    for readme in separate_readmes:

        # process readme
        lines_in_readme: typing.List[str] = []
        with open(readme, "r") as fh:
             lines_in_readme = fh.readlines()

        # update image decls
        lines_in_readme = _update_image_decl(Path(readme), lines_in_readme)

        # update python insert decls
        lines_in_readme = _update_python_insert_decls(Path(readme), lines_in_readme)

        # ensure chapter ends with '\n\
        if lines_in_readme[-1] != '\n':
            lines_in_readme.append('\n')

        # page breaks
        for i,l in enumerate(lines_in_readme):
            if l.startswith("<div style=\"page-break-before: always;\"></div>"):
                lines_in_readme[i] = "{pagebreak}\n"

        # output
        out_file: Path = Path(readme).parent / Path(readme).name.replace(".md", "_for_leanpub.md")
        with open(out_file, "w") as fh:
            for l in lines_in_readme:
                fh.write(l)

if __name__ == '__main__':
    concat_all_readmes()