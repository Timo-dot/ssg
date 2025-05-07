from textnode import *
import os
import shutil
from block_markdown import extract_title
from generate_page import generate_page, generate_pages_recursive


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
    start_copy_files("./static/", "./public")
    generate_pages_recursive("content/", "template.html", "public/")


if __name__ == "__main__":
    main()