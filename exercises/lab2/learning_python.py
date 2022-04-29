#!/usr/bin/python
from __future__ import print_function
print("Hello World!")

1 + 1
2 ** 2 ** 2 ** 2 ** 2
x=5
type(x)
x=5.0
type(x)
y = x
x, y = 17, 42
l = [1, 2, 3]
l[0]
x = [1, 3, 7]
y = x
y
x[1] = 6
y
4 ** 62 
1.0 / 2
0xBEE
hex(3054)
0b10
int('0b10',2)
bin(2)
5 % 2
5 == 6
str = "Look how easy!"
"I am %d years old, and my cat's name is %s." % (17, 'Shmulik')
chr(97)
ord('a')
"%d"%1234
len('Hello')
'look at me'.split(' ')
s = 'ugifletzet'
s[1]
# s[1] = 'G'
S = s.upper()
S.lower()

# bytes type - Python 3 equivalent for strings in Python 2
b'one'
b'one'[0]
hex(b'one'[0])
b'one'.upper()

'Hello'.index('H')
'Hello'.find('b')
x = [1, 2, 3, 4, 5]
x = x + [6]
x.append(6)
x[0] = 7
x * 3
x[1:3]
x[1::2]
x[::-2]
x = [1, 2, 3]
y = x[:]
y.append(4)
t = (1, 2, 3)
t
# t[0] = 2
(a, b, c) = (1, 2, 3)
x, y = y, x
d = {}
d[1] = "Sunday"
d
d = {1: 'Sunday', 2: 'Monday'}
1 in d
3 in d
d.keys()
d.values()
d.items()
num = 5
if num > 3:
    print (num * 2)
num = 17
if (num > 5) or (num == 15):
    print ("something")
sky = 'Blue'
if not 4 == 7:
    print ("always true")
if sky == 'Red':
    print ("Hell's rising!!")
elif sky == 'Yellow':
    print ('Just a sunny day ^_^')
elif sky == 'Green':
    print ('Go see a doctor')
else:
    print ('It appears the sky is %s' % (sky, ))

i = 0
while i < 10:
    print (i)
    i += 1
days = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
for day in days:
    print (day)
for i in range(10):
    print (i)


def func():
    print ("I am a function") # funny comment here


def f(num):
    num = 3

x = 1
f(x)
x


def func_with_defaults(x, y=5, z=17):
    return x, y, z


opened_file = open('x.txt', 'w')
opened_file.write('my first file!\n')
opened_file.close()
file = open('x.txt', 'r')
content = file.read()
file.close()


func()

cipher = "wklv phvvdjh lv qrw wrr kdug wr euhdn"
print(cipher.replace("w","t"))
# print(cipher) #notice, it is immutable
# print cipher #in python2.7 this works too
# print(cipher.replace("w","t").replace("r","o"))

plain = ""
for c in cipher:
    if c == ' ':
        plain += c
    else:
        plain += chr(ord(c) - 3)
print(plain)


# in python3 you can also do 
# cipher.translate(str.maketrans({'w':'t', 'r':'o'}))
