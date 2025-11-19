import os
import shutil

def copy_tree(source, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    items = os.listdir(source) #['folder1', 'folder2', 'file1', 'file2']

    for item in items:
        if os.path.isfile(item):
            shutil.copy(f"{source}/{item}", f"{dest}/{item}")
        if os.path.isdir(item):
            copy_tree(f"{source}/{item}", f"{dest}/{item}")

source, dest = "./static/", "./public/"
if not os.path.exists(source):
    raise Exception("Source path not found")

copy_tree(source, dest)
os.listdir(dest)

