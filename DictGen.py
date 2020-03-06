#!/usr/bin/env python3

import string as st

characters = ""

number_of_words = input("Input the number of words required: ")
print("{} words coming right up.".format(number_of_words))

def required_characters():
    global characters
    print("Include lowercase letters? ")
    ans = input("Y or N? ")
    if ans == "Y":
        characters += st.ascii_lowercase
    if ans == "N":
        exit
    print("Include uppercase letters? ")
    ans = input("Y or N? ")
    if ans == "Y":
        characters += st.ascii_uppercase
    if  ans == "N":
        exit
    

required_characters()
print(characters)

#i = 0
#while i < number_of_words:

#def word_gen(number_of_words):

print("\nExit\n")
