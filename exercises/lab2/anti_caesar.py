#!/usr/bin/python
import sys
import string


def substitute(message, translation):
    print("Substituting \"%s\" with alphabet\"%s\"" % (message, translation))
    translated = ''
    for symbol in message:
        if symbol in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            translated += translation[ord(symbol) - ord('A')].upper()
        elif symbol in 'abcdefghijklmnopqrstuvwxyz':
            translated += translation[ord(symbol) - ord('a')].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol
    print("translated into \"" + translated + "\"")
    return translated


def main(argv):
    anticaesar = string.ascii_lowercase[-3:] + string.ascii_lowercase[:-3]
    substitute(argv[1], anticaesar)


if __name__ == "__main__":
    main(sys.argv)
