import sys


def encrypt(file_object, keyValue):
    # Read a text file character by character
    for line in file_object:
        for ch in line:
            if ch != " " or ch != "." or ch != "," or ch != "\n":
                ch = encode(ch, keyValue)
            print ch,


def encode(ch, keyValue):
    # Define a latin alphabet
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    # Search in the alphabet the same word
    for i in alphabet:
        if ch == i:
            # Encode the current character
            return alphabet[(alphabet.index(i) + keyValue) % 23]


if __name__ == '__main__':
    file_object = open("catil-1.1.txt", "r")
    keyValue = int(sys.argv[1])
    encrypt(file_object, keyValue)
