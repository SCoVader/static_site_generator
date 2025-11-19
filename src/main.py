import os
import shutil

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


def main():
    source, dest = "./static/", "./public/"
    if not os.path.exists(source):
        raise Exception("Source path not found")
    
    if os.listdir(dest) != []:
            shutil.rmtree(dest)

    copy_tree(source, dest)
    os.listdir(dest)

    


if __name__ == "__main__":
    main()
    