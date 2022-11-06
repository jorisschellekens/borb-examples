from pathlib import Path
import os


def exec_file(p: Path) -> None:
    print("\texecuting %s ..." % p.name)
    os.system('python3 %s' % p)


def exec_chapter_002():
    print("executing chapter_002:")
    parent: Path = Path(__file__).parent
    exec_file(parent / Path('chapter_002/src/snippet_001.py'))
    exec_file(parent / Path('chapter_002/src/snippet_002.py'))
    exec_file(parent / Path('chapter_002/src/snippet_003.py'))
    exec_file(parent / Path('chapter_002/src/snippet_004.py'))
    exec_file(parent / Path('chapter_002/src/snippet_005.py'))
    exec_file(parent / Path('chapter_002/src/snippet_006.py'))
    exec_file(parent / Path('chapter_002/src/snippet_007.py'))
    exec_file(parent / Path('chapter_002/src/snippet_008.py'))  # expected fail due to Path issues
    exec_file(parent / Path('chapter_002/src/snippet_009.py'))
    exec_file(parent / Path('chapter_002/src/snippet_010.py'))
    exec_file(parent / Path('chapter_002/src/snippet_011.py'))
    exec_file(parent / Path('chapter_002/src/snippet_012.py'))
    exec_file(parent / Path('chapter_002/src/snippet_013.py'))
    exec_file(parent / Path('chapter_002/src/snippet_014.py'))
    exec_file(parent / Path('chapter_002/src/snippet_015.py'))
    exec_file(parent / Path('chapter_002/src/snippet_016.py'))
    exec_file(parent / Path('chapter_002/src/snippet_017.py'))
    exec_file(parent / Path('chapter_002/src/snippet_018.py'))
    exec_file(parent / Path('chapter_002/src/snippet_019.py'))
    exec_file(parent / Path('chapter_002/src/snippet_020.py'))
    exec_file(parent / Path('chapter_002/src/snippet_021.py'))
    exec_file(parent / Path('chapter_002/src/snippet_022.py'))
    exec_file(parent / Path('chapter_002/src/snippet_023.py'))
    exec_file(parent / Path('chapter_002/src/snippet_024.py'))
    exec_file(parent / Path('chapter_002/src/snippet_025.py'))
    exec_file(parent / Path('chapter_002/src/snippet_026.py'))
    exec_file(parent / Path('chapter_002/src/snippet_027.py'))
    exec_file(parent / Path('chapter_002/src/snippet_028.py'))
    exec_file(parent / Path('chapter_002/src/snippet_029.py'))  # expected fail: attempting to insert an image that is too big
    exec_file(parent / Path('chapter_002/src/snippet_030.py'))
    exec_file(parent / Path('chapter_002/src/snippet_031.py'))
    exec_file(parent / Path('chapter_002/src/snippet_032.py'))
    exec_file(parent / Path('chapter_002/src/snippet_033.py'))
    exec_file(parent / Path('chapter_002/src/snippet_034.py'))
    exec_file(parent / Path('chapter_002/src/snippet_035.py'))
    exec_file(parent / Path('chapter_002/src/snippet_036.py'))
    exec_file(parent / Path('chapter_002/src/snippet_037.py'))
    exec_file(parent / Path('chapter_002/src/snippet_038.py'))
    exec_file(parent / Path('chapter_002/src/snippet_039.py'))  # expected fail: did not set unsplash API key to valid value


def exec_chapter_003():
    print("executing chapter_003:")
    parent: Path = Path(__file__).parent
    exec_file(parent / Path('chapter_003/src/snippet_001.py'))
    exec_file(parent / Path('chapter_003/src/snippet_002.py'))
    exec_file(parent / Path('chapter_003/src/snippet_003.py'))
    exec_file(parent / Path('chapter_003/src/snippet_004.py'))
    exec_file(parent / Path('chapter_003/src/snippet_005.py'))
    exec_file(parent / Path('chapter_003/src/snippet_006.py'))
    exec_file(parent / Path('chapter_003/src/snippet_007.py'))
    exec_file(parent / Path('chapter_003/src/snippet_008.py'))
    exec_file(parent / Path('chapter_003/src/snippet_009.py'))
    exec_file(parent / Path('chapter_003/src/snippet_010.py'))
    exec_file(parent / Path('chapter_003/src/snippet_011.py'))
    exec_file(parent / Path('chapter_003/src/snippet_012.py'))
    exec_file(parent / Path('chapter_003/src/snippet_013.py'))
    exec_file(parent / Path('chapter_003/src/snippet_014.py'))
    exec_file(parent / Path('chapter_003/src/snippet_015.py'))
    exec_file(parent / Path('chapter_003/src/snippet_016.py'))
    exec_file(parent / Path('chapter_003/src/snippet_017.py'))
    exec_file(parent / Path('chapter_003/src/snippet_018.py'))
    exec_file(parent / Path('chapter_003/src/snippet_019.py'))
    exec_file(parent / Path('chapter_003/src/snippet_020.py'))


def exec_chapter_004():
    print("executing chapter_004:")
    parent: Path = Path(__file__).parent
    exec_file(parent / Path('chapter_004/src/snippet_001.py'))
    exec_file(parent / Path('chapter_004/src/snippet_002.py'))
    exec_file(parent / Path('chapter_004/src/snippet_003.py'))
    exec_file(parent / Path('chapter_004/src/snippet_004.py'))
    exec_file(parent / Path('chapter_004/src/snippet_005.py'))
    exec_file(parent / Path('chapter_004/src/snippet_006.py'))
    exec_file(parent / Path('chapter_004/src/snippet_007.py'))
    exec_file(parent / Path('chapter_004/src/snippet_008.py'))
    exec_file(parent / Path('chapter_004/src/snippet_009.py'))
    exec_file(parent / Path('chapter_004/src/snippet_010.py'))
    exec_file(parent / Path('chapter_004/src/snippet_011.py'))


def exec_chapter_005():
    print("executing chapter_005:")
    parent: Path = Path(__file__).parent
    exec_file(parent / Path('chapter_005/src/snippet_001.py'))
    exec_file(parent / Path('chapter_005/src/snippet_002.py'))
    exec_file(parent / Path('chapter_005/src/snippet_003.py'))
    exec_file(parent / Path('chapter_005/src/snippet_004.py'))
    exec_file(parent / Path('chapter_005/src/snippet_005.py'))
    exec_file(parent / Path('chapter_005/src/snippet_006.py'))
    exec_file(parent / Path('chapter_005/src/snippet_007.py'))
    exec_file(parent / Path('chapter_005/src/snippet_008.py'))
    exec_file(parent / Path('chapter_005/src/snippet_009.py'))
    exec_file(parent / Path('chapter_005/src/snippet_010.py'))
    exec_file(parent / Path('chapter_005/src/snippet_011.py'))  # expected fail: no module nltk
    exec_file(parent / Path('chapter_005/src/snippet_012.py'))
    exec_file(parent / Path('chapter_005/src/snippet_013.py'))
    exec_file(parent / Path('chapter_005/src/snippet_014.py'))
    exec_file(parent / Path('chapter_005/src/snippet_015.py'))
    exec_file(parent / Path('chapter_005/src/snippet_016.py'))
    exec_file(parent / Path('chapter_005/src/snippet_017.py'))
    exec_file(parent / Path('chapter_005/src/snippet_018.py'))
    exec_file(parent / Path('chapter_005/src/snippet_019.py'))
    exec_file(parent / Path('chapter_005/src/snippet_020.py'))
    exec_file(parent / Path('chapter_005/src/snippet_021.py'))
    exec_file(parent / Path('chapter_005/src/snippet_022.py'))
    exec_file(parent / Path('chapter_005/src/snippet_023.py'))
    exec_file(parent / Path('chapter_005/src/snippet_024.py'))
    exec_file(parent / Path('chapter_005/src/snippet_025.py'))
    exec_file(parent / Path('chapter_005/src/snippet_026.py'))
    exec_file(parent / Path('chapter_005/src/snippet_027.py'))
    exec_file(parent / Path('chapter_005/src/snippet_028.py'))
    exec_file(parent / Path('chapter_005/src/snippet_029.py'))
    exec_file(parent / Path('chapter_005/src/snippet_030.py'))
    exec_file(parent / Path('chapter_005/src/snippet_031.py'))
    exec_file(parent / Path('chapter_005/src/snippet_032.py'))
    exec_file(parent / Path('chapter_005/src/snippet_033.py'))
    exec_file(parent / Path('chapter_005/src/snippet_034.py'))
    exec_file(parent / Path('chapter_005/src/snippet_035.py'))
    exec_file(parent / Path('chapter_005/src/snippet_036.py'))


def exec_chapter_006():
    print("executing chapter_006:")
    parent: Path = Path(__file__).parent
    exec_file(parent / Path('chapter_006/src/snippet_001.py'))
    exec_file(parent / Path('chapter_006/src/snippet_002.py'))
    exec_file(parent / Path('chapter_006/src/snippet_003.py'))
    exec_file(parent / Path('chapter_006/src/snippet_004.py'))
    exec_file(parent / Path('chapter_006/src/snippet_005.py'))
    exec_file(parent / Path('chapter_006/src/snippet_006.py'))
    exec_file(parent / Path('chapter_006/src/snippet_007.py'))
    exec_file(parent / Path('chapter_006/src/snippet_008.py'))
    exec_file(parent / Path('chapter_006/src/snippet_009.py'))
    exec_file(parent / Path('chapter_006/src/snippet_010.py'))


def exec_chapter_007():
    print("executing chapter_007:")
    parent: Path = Path(__file__).parent
    exec_file(parent / Path('chapter_007/src/snippet_001.py'))
    exec_file(parent / Path('chapter_007/src/snippet_002.py'))
    exec_file(parent / Path('chapter_007/src/snippet_003.py'))
    exec_file(parent / Path('chapter_007/src/snippet_004.py'))
    exec_file(parent / Path('chapter_007/src/snippet_005.py'))
    exec_file(parent / Path('chapter_007/src/snippet_006.py'))
    exec_file(parent / Path('chapter_007/src/snippet_007.py'))
    exec_file(parent / Path('chapter_007/src/snippet_008.py'))
    exec_file(parent / Path('chapter_007/src/snippet_009.py'))
    exec_file(parent / Path('chapter_007/src/snippet_010.py'))
    exec_file(parent / Path('chapter_007/src/snippet_011.py'))


def exec_chapter_009():
    print("executing chapter_009:")
    parent: Path = Path(__file__).parent
    exec_file(parent / Path('chapter_009/src/snippet_001.py'))
    exec_file(parent / Path('chapter_009/src/snippet_002.py'))
    exec_file(parent / Path('chapter_009/src/snippet_003.py'))
    exec_file(parent / Path('chapter_009/src/snippet_004.py'))
    exec_file(parent / Path('chapter_009/src/snippet_005.py'))
    exec_file(parent / Path('chapter_009/src/snippet_006.py'))
    exec_file(parent / Path('chapter_009/src/snippet_007.py'))
    exec_file(parent / Path('chapter_009/src/snippet_008.py'))
    exec_file(parent / Path('chapter_009/src/snippet_009.py'))
    exec_file(parent / Path('chapter_009/src/snippet_010.py'))

    exec_file(parent / Path('chapter_009/src/snippet_011.py'))
    exec_file(parent / Path('chapter_009/src/snippet_012.py'))
    exec_file(parent / Path('chapter_009/src/snippet_013.py'))
    exec_file(parent / Path('chapter_009/src/snippet_014.py'))
    exec_file(parent / Path('chapter_009/src/snippet_015.py'))
    exec_file(parent / Path('chapter_009/src/snippet_016.py'))
    exec_file(parent / Path('chapter_009/src/snippet_017.py'))
    exec_file(parent / Path('chapter_009/src/snippet_018.py'))
    exec_file(parent / Path('chapter_009/src/snippet_019.py'))
    exec_file(parent / Path('chapter_009/src/snippet_020.py'))

    exec_file(parent / Path('chapter_009/src/snippet_021.py'))
    exec_file(parent / Path('chapter_009/src/snippet_022.py'))
    exec_file(parent / Path('chapter_009/src/snippet_023.py'))
    exec_file(parent / Path('chapter_009/src/snippet_024.py'))
    exec_file(parent / Path('chapter_009/src/snippet_025.py'))
    exec_file(parent / Path('chapter_009/src/snippet_026.py'))
    exec_file(parent / Path('chapter_009/src/snippet_027.py'))
    exec_file(parent / Path('chapter_009/src/snippet_028.py'))
    exec_file(parent / Path('chapter_009/src/snippet_029.py'))
    exec_file(parent / Path('chapter_009/src/snippet_030.py'))

    exec_file(parent / Path('chapter_009/src/snippet_031.py'))
    exec_file(parent / Path('chapter_009/src/snippet_032.py'))
    exec_file(parent / Path('chapter_009/src/snippet_033.py'))
    exec_file(parent / Path('chapter_009/src/snippet_034.py'))
    exec_file(parent / Path('chapter_009/src/snippet_035.py'))
    exec_file(parent / Path('chapter_009/src/snippet_036.py'))
    exec_file(parent / Path('chapter_009/src/snippet_037.py'))
    exec_file(parent / Path('chapter_009/src/snippet_038.py'))
    exec_file(parent / Path('chapter_009/src/snippet_039.py'))
    exec_file(parent / Path('chapter_009/src/snippet_040.py'))


def main():
    exec_chapter_002()
    exec_chapter_003()
    exec_chapter_004()
    exec_chapter_005()
    exec_chapter_006()
    exec_chapter_007()
    exec_chapter_009()


if __name__ == "__main__":
    main()