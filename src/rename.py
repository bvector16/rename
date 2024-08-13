import os
import sys


def main():
    DIR = os.getcwd() + '\\'
    i = 1
    list = os.listdir(DIR)
    for file in list:
        name, ext = os.path.splitext(file)
        if name in sys.argv[1:]:
            continue
        elif name in [str(i) for i in range(1, len(list)-len(sys.argv[1:])+1, 1)]:
            continue
        elif (f"{i}"+ext) in list:
            create = False
            while not create:
                i += 1
                if (f"{i}"+ext) not in list:
                    os.rename(DIR+name+ext, DIR+f"{i}"+ext)
                    create = True
        else:
            os.rename(DIR+name+ext, DIR+f"{i}"+ext)
        i += 1

if __name__ == '__main__':
    main()