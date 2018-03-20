import sys


def encrypt(file_object, keyValue):
    for line in file_object:
        for ch in line:
            if ch != ' ' or ch != '.' or ch != ',' or ch != '"':
                print encode(ch, keyValue),


def encode(ch, keyValue):
    newCh = (ord(ch)+keyValue)
    if newCh == 'j' or newCh == 'w' or newCh == 'k':
        newCh == (ord(ch)+keyValue)
    if newCh > ord('z'):
        newCh -= 26

    return chr(newCh)


if __name__ == '__main__':
    file_object = open("catil-1.1.txt", "r")
    keyValue = int(sys.argv[1])
    encrypt(file_object, keyValue)
