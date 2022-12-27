# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kai Elmore
# Section:      545
# Team:         N/A
# Assignment:   Lab 7b Program 1
# Date:         10/9/2020
#

print('This program translates a given word from english into Pig Latin')

# Variables
list_digraphs = ['bl','br','ch','ck','cl','cr','dr','fl','fr','gh', \
                 'gl', 'gr', 'ng', 'ph', 'pl', 'pr', 'qu', 'sc', 'sh', 'sk', \
                'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr']
list_trigraphs = ['sch','scr','shr','spl','spr','squ','str','thr']
list_vowels = ['a','e','i','o','u','y']
word = input('Enter the word you want translated here: ')
list_word = list(word)
string_word = ''



# Loop to translate
while word != 'stop':
    if list_word[0] in list_vowels:
        list_word.append('yay')
        for letter in list_word:
            string_word += letter
        print('Original word:', word)
        print('Pig Lating translation:', string_word)
    elif list_word[0] + list_word[1] + list_word[2] in list_trigraphs:
        list_word.append(word[0])
        list_word.append(word[1])
        list_word.append(word[2])
        list_word.append('ay')
        list_word[0:3] = []
        for letter in list_word:
            string_word += letter
        print('Original word:', word)
        print('Pig Lating translation:', string_word)
    elif list_word[0] + list_word[1] in list_digraphs:
        list_word.append(word[0])
        list_word.append(word[1])
        list_word.append('ay')
        list_word[0:2] = []
        for letter in list_word:
            string_word += letter
        print('Original word:', word)
        print('Pig Lating translation:', string_word)
    else:
        list_word.append(word[0])
        list_word.append('ay')
        list_word.pop(0)
        for letter in list_word:
            string_word += letter
        print('Original word:', word)
        print('Pig Lating translation:', string_word)
    string_word = ''
    word = input('Enter the word you want translated here: ')
    list_word = list(word)
    
