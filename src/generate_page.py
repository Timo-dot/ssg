from block_markdown import *
import os


def generate_page(from_path, template_path, dst_path):
    print(f"Generating page from {from_path} to {dst_path} using {template_path}")
    with open(from_path, 'r') as f:
        md = f.read()
    with open(template_path, 'r') as f:
        tmpl = f.read()
    html_string = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    tmpl.replace("\{\{ Title \}\}", title)
    tmpl.replace("\{\{ Content \}\}", html_string)
    dirs = dst_path.split("/")
    path = dirs[0]
    if not os.path.exists(path):
        if not os.path.isfile(path):
            os.mkdir(path)
        else:
            open(path, 'x')
    for dir in dirs[1:-1]:
        path = os.path.join(path, dir)
        if not os.path.exists(path):
            if not os.path.isfile(path):
                os.mkdir(path)
    with open(os.path.join(path, dirs[-1].replace(".md", ".html")), 'w') as f:
        f.write(html_string)


def generate_pages_recursive(dir_path_content, template_path, dst_dir_path):
    if os.path.isfile(dir_path_content):
        generate_page(dir_path_content, template_path, dst_dir_path)
        return
    for entry in os.listdir(dir_path_content):
        generate_pages_recursive(
            os.path.join(dir_path_content, entry),
            template_path,
            os.path.join(dst_dir_path, entry)
        )