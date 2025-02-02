import pathlib


files = pathlib.Path('./final_project')

for file in files.iterdir():
    if file.is_file():
        with open(file, encoding='windows-1251') as f:
            print(''.join(f.readlines()[:10]))
