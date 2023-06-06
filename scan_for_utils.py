import mmap
from pathlib import Path


def scan_dir_for_text_pattern(pattern: str = 'notebook_utils'):
    """
    Scan files in the current directory for a text pattern.
    """
    list_using = []
    list_free = []
    for path in Path("./notebooks").rglob('*.ipynb'):
        if '.ipynb_checkpoints' in str(path):
            continue
        if search_for_line_in_file(path, pattern):
            list_using.append(path)
        else:
            list_free.append(path)
    return sorted(list_using), sorted(list_free)


def search_for_line_in_file(path: Path, line: str) -> bool:
    """
    Search for a line in a file.
    """
    with open(path, 'rb', 0) as file:
        s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        if s.find(bytes(line, 'utf-8')) != -1:
            return True
    return False


scan_dir_for_text_pattern()
