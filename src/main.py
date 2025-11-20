import os
import shutil
from block_markdown import (markdown_to_html_node)


def copy_tree(source, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)
    
    items = os.listdir(source) #['folder1', 'folder2', 'file1', 'file2']
    for item in items:
        print(f"{item}")
        item_path = f"{source}/{item}"
        if os.path.isfile(item_path):
            print(f"{item} is file")
            shutil.copy(item_path, f"{dest}/{item}")
        if os.path.isdir(item_path):
            print(f"{item} is dir")
            copy_tree(item_path, f"{dest}/{item}")

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip("# ")
    raise Exception("No title found")

def cleanup_n_copy_content(src='./static/', dst = './public/'):
    if not os.path.exists(src):
        raise Exception("Source path not found")

    if not os.path.exists(dst):
        os.mkdir(dst)

    if os.listdir(dst) != []:
        shutil.rmtree(dst)

    copy_tree(src, dst)
    os.listdir(dst)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as markdown_file:
        markdown = markdown_file.read()
    with open(template_path) as template_file:
        template = template_file.read()

    node = markdown_to_html_node(markdown)
    html = node.to_html()
    title = extract_title(markdown)
    titled = template.replace(r"{{ Title }}", title)
    full = titled.replace(r"{{ Content }}", html)

    with open(dest_path, 'x') as output:
        output.write(full)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise Exception("Invalid content folder")
    items = os.listdir(dir_path_content)
    for item in items:
        src = os.path.join(dir_path_content, item)
        dst = os.path.join(dest_dir_path, item)
        if os.path.isdir(src):
            if not os.path.exists(dst):
                os.mkdir(dst)
            generate_pages_recursive(src, template_path, dst)
        if os.path.isfile(src):
            dst = f'{dst[0:-3]}.html'
            generate_page(src, template_path, dst)

def main():
    source = "./content/"
    destination = "./public/"
    template = "./template.html"
    cleanup_n_copy_content()
    generate_pages_recursive(source, template, destination)
    

if __name__ == "__main__":
    main()
    