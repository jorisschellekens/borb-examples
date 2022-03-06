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
            ls_out.append("![%s](%s)" % (d, str(root.parent / p)))
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
# TABLE OF CONTENTS
#

def _build_table_of_contents(ls: typing.List[str]) -> typing.List[str]:

    toc_lines: typing.List[str] = ["# Table of Contents", "\n","\n"]
    p = re.compile("#+ *([1-9]+[\.0-9]*) (.+)\n")

    for l in ls:
        m: re.Match = p.match(l)
        if m is not None:
            # determine indent level
            indent_level: int = 0
            while indent_level < len(l) and l[indent_level] == "#":
                indent_level += 1

            # determine initial tabs
            tabs = "  " * (indent_level - 1) if indent_level >= 1 else ""

            # determine number
            number: str = m.group(1)

            # determine text
            title: str = m.group(2)

            # determine link
            link: str = "#" + number.replace(".", "") + "-" + re.sub("[^a-z _\-]", "", title.lower()).replace(" ","-")

            toc_lines.append(tabs + number + " [" + title + "](" + link + ")  \n")

    # return
    toc_lines.append('\n')
    toc_lines.append('<div style=\"page-break-before: always;\"></div>\n')
    toc_lines.append('\n')
    toc_lines.extend(ls)

    # return
    return toc_lines

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

        # concat
        lines_concat.extend(lines_in_readme)

    # build toc
    lines_concat = _build_table_of_contents(lines_concat)

    # write
    with open("README.md", "w") as fh:
        for l in lines_concat:
            fh.write(l)


if __name__ == '__main__':
    concat_all_readmes()