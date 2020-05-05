import os
import shutil
import sys

def order_files_of_path(root_path):
    old_new_dirs = []
    print(f'path: {root_path}')
    for dir_file in os.listdir(root_path):
        if os.path.isdir(os.path.join(root_path, dir_file)):
            try:
                file_names = [_dir_file for _dir_file in os.listdir(os.path.join(root_path, dir_file)) if os.path.isfile(os.path.join(root_path, dir_file, _dir_file)) and '第' in _dir_file and '集' in _dir_file]
                if len(file_names) > 0:
                    old_path = os.path.join(root_path, dir_file)
                    new_path = os.path.join(root_path, dir_file + '_new')
                    old_new_dirs.append((old_path, new_path))
                    os.mkdir(os.path.join(root_path, dir_file + '_new'))
                    for file_name in sorted(file_names, reverse=False, key=lambda x: int(x[x.index('第') + 1:x.index('集')])):
                        shutil.move(os.path.join(old_path, file_name), os.path.join(new_path, file_name))
                        print(f'Move {file_name}')
            except PermissionError:
                pass
    for old_path, new_path in old_new_dirs:
        os.rename(new_path, old_path)
        print(f'Rename {old_path}')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        path = os.getcwd()
    else:
        path = sys.argv[1]
    order_files_of_path(path)
