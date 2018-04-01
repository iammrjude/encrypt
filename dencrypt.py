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


def encode(ch, keyValue,):
    # Define a latin alphabet
    alphabet_a = ["b", "d", "f", "h", "l","n", "p", "r", "t", "v", "y"]
    alphabet_b = ["a", "c", "e", "g", "i", "m", "o", "q", "s", "u", "x", "z"]
    # Search in the alphabet the same word
    for i in alphabet_a:
        if ch == i:
            # Encode the current character
            return alphabet_a[(alphabet_a.index(i) - keyValue) % 10]

    for i in alphabet_b:
        if ch == i:
            # Encode the current character
            if (alphabet_b.index(i) - keyValue * 2) % 11 < alphabet_b.index(i - i)
                return alphabet_b[((alphabet_b.index(i) - keyValue*2) % 11)+11]
            else
                return alphabet_b[(alphabet_b.index(i) - keyValue * 2) % 11]



def isExeption(ch):
    return (ch == " " or ch == "," or ch == "." or ch == "\n" or ch == "?"
            or ch == "!" or ch == ":" or ch == "\"" or ch == ';')


if __name__ == '__main__':
    originalText = open(sys.argv[2], 'r')
    encryptedText = open(sys.argv[3], 'w')
    keyValue = int(sys.argv[1])
    text = ''
    encrypt(originalText, keyValue, originalText.readline(), text)
