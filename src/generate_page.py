from block_markdown import *
import os


def generate_page(from_path, template_path, dst_path, basepath):
    print(f"Generating page from {from_path} to {dst_path} using {template_path}")
    with open(from_path, 'r') as f:
        md = f.read()
    with open(template_path, 'r') as f:
        tmpl = f.read()
    html_string = markdown_to_html_node(md).to_html()
    #print(html_string)
    title = extract_title(md)
    #print(title)
    html_title = tmpl.replace("{{ Title }}", title)
    #print(html_title)
    html_content = html_title.replace("{{ Content }}", html_string)
    #print(html_content)
    html_href = html_content.replace("href=\"/", f"href=\"{basepath}")
    #print(html_href)
    html_full = html_href.replace("src=\"/", f"src=\"{basepath}")
    #print(html_full)
    dirs = dst_path.split("/")
    path = dirs[0]
    #print(f"path={path}")
    if not os.path.exists(path):
        if not os.path.isfile(path):
            os.mkdir(path)
        else:
            open(path, 'x')
    for dir in dirs[1:-1]:
        path = os.path.join(path, dir)
        #print(f"path={path}")
        if not os.path.exists(path):
            if not os.path.isfile(path):
                os.mkdir(path)
    path = os.path.join(path, dirs[-1].replace(".md", ".html"))
    #print(f"path={path}")
    with open(path, 'w') as f:
        f.write(html_full)


def generate_pages_recursive(dir_path_content, template_path, dst_dir_path, basepath):
    if os.path.isfile(dir_path_content):
        generate_page(dir_path_content, template_path, dst_dir_path, basepath)
        return
    for entry in os.listdir(dir_path_content):
        generate_pages_recursive(
            os.path.join(dir_path_content, entry),
            template_path,
            os.path.join(dst_dir_path, entry),
            basepath
        )