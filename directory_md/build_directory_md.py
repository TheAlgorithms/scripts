#!/usr/bin/env python3

import os
import sys
from typing import Iterator

if ".py" in sys.argv[0]:
    sys.argv.pop(0)


if len(sys.argv) not in (3, 4, 5):
    print(
        "Arguments:\n"
        "[0] - Language\n"
        "[1] - Base path\n"
        "[2] - Allowed filenames\n"
        "[3] - Files or folders to ignore (optional)\n"
        "[4] - Folders to ignore, but include children (optional)"
    )
    sys.exit()

ignore = []
skip = []
if len(sys.argv) == 4:
    ignore = sys.argv[3].split(",")
if len(sys.argv) == 5:
    skip = sys.argv[4].split(",")

URL_BASE = f"https://github.com/TheAlgorithms/{sys.argv[0]}/blob/HEAD"


def good_file_paths(top_dir: str = ".") -> Iterator[str]:
    for dir_path, dir_names, filenames in os.walk(top_dir):
        dir_names[:] = [d for d in dir_names if d != "scripts" and d[0] not in "._"]
        for filename in filenames:
            if filename == "__init__.py":
                continue
            if any(
                e.lower() in os.path.join(dir_path, filename).lower() for e in ignore
            ):
                continue
            if os.path.splitext(filename)[1] in sys.argv[2].split(","):
                path = os.path.join(dir_path, filename).lstrip(".").lstrip("/")
                for e in skip:
                    path = path.replace(e + "/", "")
                    path = path.replace(e + "\\", "")
                yield path


def md_prefix(i):
    return f"{i * '  '}*" if i else "\n##"


def print_path(old_path: str, new_path: str) -> str:
    old_parts = old_path.split(os.sep)
    for i, new_part in enumerate(new_path.split(os.sep)):
        if i + 1 > len(old_parts) or old_parts[i] != new_part:
            if new_part:
                print(f"{md_prefix(i)} {new_part.replace('_', ' ').title()}")
    return new_path


def print_directory_md(top_dir: str = ".") -> None:
    old_path = ""
    for filepath in sorted(good_file_paths(top_dir)):
        filepath, filename = os.path.split(filepath)
        if filepath != old_path:
            old_path = print_path(old_path, filepath)
        indent = (filepath.count(os.sep) + 1) if filepath else 0
        url = "/".join((URL_BASE, filepath, filename)).replace(" ", "%20")
        filename = os.path.splitext(filename.replace("_", " ").title())[0]
        print(f"{md_prefix(indent)} [{filename}]({url})")


if __name__ == "__main__":
    print_directory_md(sys.argv[1])
