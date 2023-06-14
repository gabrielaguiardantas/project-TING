import sys
import os


def txt_importer(path_file):
    correct_txt = []

    if str(path_file[-4:]).find(".txt") == -1:
        print("Formato inválido", file=sys.stderr)
        return
    elif not os.path.exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return
    else:
        txt_file = open(path_file).readlines()
        correct_txt.append(txt_file[0][:-1])
        correct_txt.append(txt_file[1][:-1])
        correct_txt.append(txt_file[2])

        return correct_txt
