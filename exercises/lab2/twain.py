from freqAnalysis import *
m = open("3190.txt","rt").read()
c = substitute(m, 'ZWSJTOLRQBFGEXDAMUHICNKPVY')
# print(c)
guess = getTranslationAlphabet(c)
print guess
# # FJUOMKLHTDYPQVWXIRCESGBNZA
# # add calls to swat here like
guess = swap(guess, 'Y', 'W')
guess = swap(guess, 'R', 'H')
guess = swap(guess, 'F', 'P')
guess = swap(guess, 'R', 'S')
guess = swap(guess, 'Y', 'F')
guess = swap(guess, 'Y', 'G')
print  substitute(c, guess)

