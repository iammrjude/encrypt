import sys


def encrypt(file_object):
    for line in file_object:
        for ch in line:
            if ch != ' ':
                print ch



if __name__ == '__main__':
    file_object = open("catil-1.1.txt", "r")
    encrypt(file_object)
