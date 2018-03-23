import sys


def encrypt(originalText, keyValue):
    text = ''
    # Read a text file character by character
    for line in originalText:
        for ch in line:
            if isExeption(ch):
                text += ch
            # Upper case
            elif ch.isupper():
                ch = ch.lower()
                newCh = str(encode(ch, keyValue))
                newCh = newCh.upper()
                text += newCh
            else:
                newCh = str(encode(ch, keyValue))
                text += newCh
    encryptedText.write(text)
    encryptedText.close()


def encode(ch, keyValue):
    # Define a latin alphabet
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
    # Search in the alphabet the same word
    for i in alphabet:
        if ch == i:
            # Encode the current character
            return alphabet[(alphabet.index(i) + keyValue) % 23]


def isExeption(ch):
    return (ch == " " or ch == "," or ch == "." or ch == "\n" or ch == "?"
            or ch == "!" or ch == ":")


if __name__ == '__main__':
    originalText = open(sys.argv[2], 'r')
    encryptedText = open(sys.argv[3], 'w')
    keyValue = int(sys.argv[1])
    encrypt(originalText, keyValue)
