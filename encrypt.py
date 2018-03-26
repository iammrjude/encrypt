import sys


def encrypt(originalText, keyValue, line, text):
    try:
        # Read a text file character by character
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
        # Recursive method reading line by line
        return encrypt(originalText, keyValue, originalText.next(), text)
    # EOF
    except StopIteration:
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
    text = ''
    encrypt(originalText, keyValue, originalText.readline(), text)
