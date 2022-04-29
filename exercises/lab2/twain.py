from freqAnalysis import *
m = open("3190.txt","rt").read()
c = substitute(m, 'ZWSJTOLRQBFGEXDAMUHICNKPVY')
# print(c)
guess = getTranslationAlphabet(c)
print (guess)
# # FJUOMKLHTDYPQVWXIRCESGBNZA
guess = swap(guess, 'Y', 'W')
# # add calls to swap here like
print  (substitute(c, guess))

