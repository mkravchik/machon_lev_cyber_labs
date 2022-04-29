from freqAnalysis import *
m = open("3190.txt","rt").read()
c = substitute(m, 'ZWSJTOLRQBFGEXDAMUHICNKPVY')
# print(c)
guess = getTranslationAlphabet(c)
print (guess)
# # # FJUOMKLHTDYPQVWXIRCESGBNZA
guess = swap(guess, 'Y', 'W')
# guess = swap(guess, 'H', 'S')
guess = swap(guess, 'R', 'H')
guess = swap(guess, 'F', 'P')
guess = swap(guess, 'R', 'S')
guess = swap(guess, 'F', 'G')
guess = swap(guess, 'Y', 'F')
# # add calls to swap here like
print  (substitute(c, guess))

