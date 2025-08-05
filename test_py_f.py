import os

for root, dirs, files in os.walk('.'):
    # print(f"Директория: {root}")
    # print(f"Поддиректории: {dirs}")
    # print(f"Файлы: {files}")
    levels = root.split(os.sep)  # ['.', '.git', 'hooks'] тут раздробленно пишутся названия подкаталогов соответствуя количеству уровней
    depth = len(levels) - 1 # тут у нас числами назначаются уровни директорий

    print(f"Директория: {depth.sort()}")
