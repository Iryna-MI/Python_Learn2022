import random
from random import randrange
import string

def function(n):
   mydict = {}
   ABC = ['abcdefghijklmnopqrstuvwxyz']
   for i in range(n):
      for letter in string.ascii_lowercase:
         #mydict[str(i)] = randrange(10)
         mydict[letter] = randrange(10)
   return mydict

print(function(5))

letters = string.ascii_lowercase
print(letters)
mydict1 = {}
mydict2= {}
for i in range(5):
   mydict1[random.choice(string.ascii_letters).lower()] = randrange(100)
   #mydict2[random.choice(string.ascii_letters).lower()] = randrange(100)

mylist = []
mylist.append(mydict1)
#mylist.append(mydict2)
print (mydict1)
#print (mydict2)
print(mylist)

