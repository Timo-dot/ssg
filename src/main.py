from textnode import *
import os
import shutil
from generate_page import generate_pages_recursive
import sys


def copy_files(path, dst):
    if not os.path.exists(path):
        return
    if os.path.isfile(path):
        shutil.copy(path, dst)
        print(f"{path} to {dst}")
        return
    else:
        dir = path.split("/")[-1]
        if dir != "static":
            dst = os.path.join(dst, dir)
            if not os.path.exists(dst):
                os.mkdir(dst)
        for entry in os.listdir(path):
            copy_files(os.path.join(path, entry), dst)
    

def start_copy_files(path, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
        print(f"Deleting {dst}")
    os.mkdir(dst)
    copy_files(path, dst)


def main():
    basepath = "/" if len(sys.argv) == 1 else sys.argv[1]
    start_copy_files("static/", "docs/")
    generate_pages_recursive("content/", "template.html", "docs/", basepath)


if __name__ == "__main__":
    main()