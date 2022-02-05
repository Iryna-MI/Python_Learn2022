import random
from random import randrange
import string


mydict = {}
mylist = []
for i in range(random.randint(2, 10)):
   mydict[random.choice(string.ascii_letters).lower()] = randrange(100) #random letter for keys
   mylist.append(mydict) #add dictionary to the list

print("Task1. List of random number of dicts ", mylist)

# initialize the final dictionary
final_dict, tmp_dict = {},  {}

#Transform from list of dicts into dict of lists.
for dictionary in mylist:
  for k, v in dictionary.items():
    tmp_dict.setdefault(k, []).append(v) #returns the key value available in the dictionary and if given key is not available then it will return provided default value.

#choose the biggest one
for k, v in tmp_dict.items():
  if len(v) > 1:
    final_dict[k+"_"+str(v.index(max(v))+1)] = max(v)
  else: final_dict[k] = v[0]

# print result
print("Task2. Common dictionary:", final_dict)





