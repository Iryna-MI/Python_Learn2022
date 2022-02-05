# Module 3. String Object

import re

# copy homework text to variable
start_text =  """homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# normalize text
# ^ (Caret.) Matches the start of the string, and in MULTILINE mode also matches immediately after each newline.
# (Dot.) In the default mode, this matches any character except a newline. If the DOTALL flag has been specified, this matches any character including a newline.
# [] Used to indicate a set of characters.
# * matches preceding match zero or more times
# $ matches position just after the last character of the string
# \s= space
# \n = new line
# \t =tab
list_of_text = re.split(r'(^|[.]\s|\n\t)', start_text)

normalized_text = ''
for i in list_of_text:
    normalized_text += i.capitalize()

# replace misspelling in normalized text
normalized_text_without_misspelling = normalized_text.replace(' iz ', ' is ')


# create sentence with last words of each existing sentence
sentence_of_last_words = ''
for sentence in normalized_text_without_misspelling.split('.'):
    # split by space and convert string to list and
    lis = list(sentence.split(" "))
    # length of list
    length = len(lis)
    # last word of the sentence = last element in list
    sentence_of_last_words += str(lis[length-1]) + ' '
print('\n\t' + "Sentence with last words of each existing sentence: ", sentence_of_last_words.capitalize())

# calculate number of whitespace character
whitespace_characters = len(re.findall(r'\s', start_text))
print('\n\t' + 'Number of whitespace characters: not 87 but', whitespace_characters)


