import random
from random import randrange
import string
import re

#dictionaries creation
def dicts (num_dicts,values_range):
    dicts_List = []
    for i in range(random.randint(2, num_dicts)): # random number of dictionaries
        size    = random.randint(1, 26)    # random dictionary size = not more than alphabet letters
        keys    = random.sample(string.ascii_lowercase,size)  # random letters
        values  = (random.randint(1, values_range) for n in range(size)) # random numbers
        mydict = dict(zip(keys, values)) # zip() enable to create dic joining the lists of keys and values
        dicts_List.append(mydict)
    return dicts_List

#create general dictionary
def create_general_dictionary (dict_list):
    # initialize the final dictionary
    final_dict, tmp_dict = {},  {}
    #Transform from list of dicts into dict of lists.
    for dictionary in dict_list:
        for k, v in dictionary.items():
        #returns the key value available in the dictionary and if given key is not available then it will return provided default value.
            tmp_dict.setdefault(k, []).append(v)
    #choose the biggest one
    for k, v in tmp_dict.items():
        if len(v) > 1:
            final_dict[k+"_"+str(v.index(max(v))+1)] = max(v)
        else: final_dict[k] = v[0]
    return final_dict





# normalize text
# ^ (Caret.) Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.
# (Dot.) In the default mode, this matches any character except a newline. If the DOTALL flag has been specified, this matches any character including a newline.
# [] Used to indicate a set of characters.
# * matches preceding match zero or more times
# $ matches position just after the last character of the string
# \s= space
# \n = new line
# \t =tab
def normalize_text (text):
    list_of_text = re.split(r'(^|[.]\s|\n\t)', start_text)
    normalized_text = ''
    for i in list_of_text:
        normalized_text += i.capitalize()
        # replace misspelling in normalized text
    normalized_text_without_misspelling = normalized_text.replace(' iz ', ' is ')
    return normalized_text_without_misspelling


# create sentence with last words of each existing sentence
def new_sentence(text):
    sentence_of_last_words = ''
    for sentence in text.split('.'):
        # split by space and convert string to list and
        lis = list(sentence.split(" "))
        # length of list
        length = len(lis)
        # last word of the sentence = last element in list
        sentence_of_last_words += str(lis[length-1]) + ' '
    return sentence_of_last_words.capitalize()

# calculate number of whitespace character
def whitespaces_culc(text):
    whitespace_characters = len(re.findall(r'\s', text))
    return whitespace_characters

# copy homework text to variable
start_text =  """homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


# print result lesson3 task1.
# function dicts parameters: 1)num_dicts - range of number of dicts; 2) values_range - range for dicts values
try:
    print ("Lesson3.Task1. List of random number of dicts: ", dicts(3, 100))
except:
    print("Something went wrong")


#print result lesson3 task2.
#function create_general_dictionary parameter : list of dictionaries
try:
    print("Lesson3.Task2. Common dictionary:", create_general_dictionary (dicts(3, 100)))
except:
    print("Something went wrong")


#print result lesson4 task1: Sentence with last words of each existing sentence
try:
    normalized_text = normalize_text (start_text)
except:
    print("Something happen to text :(")

try:
    print('\n' + "Lesson4.Task1. Sentence with last words of each existing sentence: ", new_sentence(normalized_text))
except:
    print("Something went wrong")

#print result lesson4 task3 number of whitespaces
try:
    print('\n' + 'Lesson4.Task2. Number of whitespace characters: not 87 but', whitespaces_culc(normalized_text))
except:
    print("Something went wrong")
