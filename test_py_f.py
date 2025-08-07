import os

for root, dirs, files in os.walk('.'):
    dirs.sort()
    files.sort()
    
    levels = root.split(os.sep)
    dir_ = root.split(os.sep)[-1]
    depth = len(levels) - 1 
    
    if depth == 0:
        print(f"{dir_}")
        root_files = files
        continue
    
    indent = '│   ' * (depth - 1)
    prefix = '├──' 
    print(f"{indent}{prefix} {dir_}")

    for i, file in enumerate(files):
        indentF = '│   ' * (depth)
        last_file = (i == (len(files) - 1))
        prefix = '└──' if last_file else '├──' 
        print(f"{indentF}{prefix} {file}") 
    
for i, fIle in enumerate(root_files):
    indentX = '│   ' * (depth - 2)
    last_filE = (i == (len(root_files) - 1))
    Prefix = '└──' if last_filE else '├──' 
    print(f"{indentX}{Prefix} {fIle}") 
