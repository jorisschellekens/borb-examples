from pathlib import Path
import typing

#
# !! CAUTION !!
# When set to True, this script will output the proposed renames but will NOT execute them.
# When set to False, this script executes the renames.
#
debug_mode: bool = False


def insert_example_at(n: int) -> None:
    """
    This method renames the example files, to ensure a new example can be fitted at a number that was already in use
    :param n:   the number at which the new example is to be inserted
    :return:    None
    """
    example_dir: Path = Path(__file__).parent / "example"
    assert example_dir.exists()

    # get all python files
    python_files: typing.List[Path] = [x for x in example_dir.iterdir() if x.name.endswith(".py") and x.name.startswith("example_")]

    # determine new names (in bulk)
    to_rename: typing.List[typing.Tuple[int, Path, Path]] = []
    for f in python_files:

        # determine what the number of the file should be
        old_number: int = int(f.name.replace("example_", "").replace(".py",""))
        if old_number < n:
            continue

        # determine new number (as str)
        new_number_str: str = str(old_number + 1)
        while len(new_number_str) < 3:
            new_number_str = "0" + new_number_str

        # determine the path of the file
        new_path: Path = f.parent / ("example_%s.py" % new_number_str)

        # rename
        to_rename.append((old_number, f, new_path))

    # sort to_rename (to ensure we perform the rename in the right order)
    to_rename.sort(key=lambda x:x[0], reverse=True)

    # execute the rename
    for t in to_rename:
        print("[PY] renaming %s to %s .." % (t[1].name, t[2].name))
        if not debug_mode:
            t[1].rename(t[2])


def insert_img_at(n: int) -> None:
    """
    This method renames the image files, to ensure one or more new images can be fitted at a number that was already in use
    :param n:   the number at which the new image(s) is/are to be inserted
    :return:    None
    """

    img_dir: Path = Path(__file__).parent / "img"
    assert img_dir.exists()

    # get all python files
    python_files: typing.List[Path] = [x for x in img_dir.iterdir() if x.name.endswith(".png") and x.name.startswith("borb_in_action_example_")]

    # determine new names (in bulk)
    to_rename: typing.List[typing.Tuple[int, Path, Path]] = []
    for f in python_files:

        # determine what the number of the file should be
        old_name: str = f.name
        old_number: int = int(old_name.replace(".png", "").split("_")[4])
        if old_number < n:
            continue

        # determine old number (as str)
        old_number_str: str = str(old_number)
        while len(old_number_str) < 3:
            old_number_str = "0" + old_number_str

        # determine new number (as str)
        new_number_str: str = str(old_number + 1)
        while len(new_number_str) < 3:
            new_number_str = "0" + new_number_str

        # determine the path of the file
        new_path: Path = f.parent / (old_name.replace(old_number_str, new_number_str))

        # rename
        to_rename.append((old_number, f, new_path))

    # sort to_rename (to ensure we perform the rename in the right order)
    to_rename.sort(key=lambda x:x[0], reverse=True)

    # execute the rename
    for t in to_rename:
        print("[PNG] renaming %s to %s .." % (t[1].name, t[2].name))
        if not debug_mode:
            t[1].rename(t[2])

    # read borb_in_action.md
    for md_name in ["borb_in_action_01.md",
              "borb_in_action_02.md",
              "borb_in_action_03.md",
              "borb_in_action_04.md",
              "borb_in_action_05.md",
              "borb_in_action_06.md"]:

        # get all text
        md_text: str = ""
        md_file: Path = Path(__file__).parent / md_name
        assert md_file.exists()
        with open(md_file, "r") as md_file_handle:
            md_text = md_file_handle.read()

        # rename
        print("[MD] Updating %s" % md_name)
        for t in to_rename:
            print("[MD] Replacing %s for %s .." % (t[1].name, t[2].name))
            if not debug_mode:
                while t[1].name in md_text:
                    md_text = md_text.replace(t[1].name, t[2].name)

        # write borb_in_action.md
        if not debug_mode:
            with open(md_file, "w") as md_file_handle:
                md_file_handle.write(md_text)


def main() -> None:
    n: int = 54
    insert_example_at(n)
    #insert_img_at(n)


if __name__ == "__main__":
    main()