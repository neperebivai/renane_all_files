import os
from random import randrange

path = os.getcwd()


def rename_files(path):
    for root, directories, files in os.walk(path):
        try:
            for file in files:
                file_path = os.path.join(root, file)
                prefix = randrange(10)
                new_file_path = os.path.join(root, f'{prefix}' + file)
                os.rename(file_path, new_file_path)
        except Exception:
            return
`

if __name__ == "__main__":
    rename_files(path)
