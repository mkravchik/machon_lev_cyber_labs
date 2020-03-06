#!/usr/bin/python
from __future__ import print_function
import operator

# frequency taken from http://en.wikipedia.org/wiki/Letter_frequency
englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99,
                     'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
                     'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def getLetterCount(message):
    # Returns a dictionary with keys of single letters and values of the
    # count of how many times they appear in the message parameter.
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
                   'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                   'Y': 0, 'Z': 0}
    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1
    return letterCount


def getItemAtIndexZero(x):
    return x[0]


def getFrequencyOrder(message):
    # Returns a string of the alphabet letters arranged in order of most
    # frequently occurring in the message parameter.

    # first, get a dictionary of each letter and its frequency count
    letterToFreq = getLetterCount(message)

    # second, make a dictionary of each frequency count to each letter(s)
    # with that frequency
    freqToLetter = {}
    for letter in LETTERS:
        if letterToFreq[letter] not in freqToLetter:
            freqToLetter[letterToFreq[letter]] = [letter]
        else:
            freqToLetter[letterToFreq[letter]].append(letter)

    # third, put each list of letters in reverse "ETAOIN" order, and then
    # convert it to a string
    for freq in freqToLetter:
        freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
        freqToLetter[freq] = ''.join(freqToLetter[freq])

    # fourth, convert the freqToLetter dictionary to a list of tuple
    # pairs (key, value), then sort them
    freqPairs = list(freqToLetter.items())
    freqPairs.sort(key=getItemAtIndexZero, reverse=True)

    # fifth, now that the letters are ordered by frequency, extract all
    # the letters for the final string
    freqOrder = []
    for freqPair in freqPairs:
        freqOrder.append(freqPair[1])

    return ''.join(freqOrder)


def getTranslationAlphabet(message):
    # Return a tentative translation alphabet based on letter frequences
    # first, get a frequency order for the message
    freqOrder = getFrequencyOrder(message)

    # second map the canonical frequences to the actual
    # For example, the actual order is MEHFTVCSPOBURQGKLZXJYWDNIA
    # The canonical is ETAOINSHRDLCUMWFGYPBVKJXQZ
    # So we map M to E, E to T, etc.
    transAlpha = ['-'] * len(freqOrder)
    for i in range(len(freqOrder)):
        transAlpha[ord(freqOrder[i]) - ord('A')] = ETAOIN[i]
    # print transAlpha
    return ''.join(transAlpha)


def getWordsCount(message, wlen):
    wc = {}
    for w in message.split():
        if len(w) != wlen:
            continue
        if w in wc:
            wc[w] += 1
        else:
            wc[w] = 1
    return sorted(wc.iteritems(), key=operator.itemgetter(1), reverse=True)


def substitute(message, translation):
    print("Substituting %s with %s alphabet" % (message, translation))
    translated = ''
    for symbol in message:
        if symbol in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            translated += translation[ord(symbol) - ord('A')].upper()
        elif symbol in 'abcdefghijklmnopqrstuvwxyz':
            translated += translation[ord(symbol) - ord('a')].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol
    print("translated into \n" + translated)
    # print getWordsCount(translated, 1)
    # print getWordsCount(translated, 2)
    # print getWordsCount(translated, 3)
    return translated


def swap(s, let1, let2):
    return s.replace(let1, '?').replace(let2, let1).replace('?', let2)
