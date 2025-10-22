#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True


# get a sentence from user and check if it meets requirements 
def get_sentence(): 
    while True: 
        try: 
            sentence = str(input("Enter a sentence: "))
            if is_sentence(sentence) is True: 
                return (sentence)
            else: 
                print("Please enter a valid sentence.")
        except: 
            printf("Please enter a valid sentence.")

# calculates the frequencies 
def calculate_frequencies(sentence):
    sentence = sentence.lower() 
    accepted_char = "abcdefghijklmnopqrstuvwxyz "

    for character in sentence:
        if character not in accepted_char:
            sentence =  sentence.replace(character, "")

    # Track the number of times each word appears 
    sep_words = sentence.split(" ")

    words_list = []
    words_count = []
    for word in sep_words: 
        if word not in words_list: 
            words_list.append(word)
            words_count.append(1)
        else: 
            count_index = words_list.index(word)
            words_count[count_index] += 1
    return (words_list, words_count)
# output frequencies 
def print_frequencies(words, frequencies):
    for i in range(len(words)):
        print(f"{words[i]}: {frequencies[i]}")


# Run the functions 
sentence = get_sentence()
words, frequencies = calculate_frequencies(sentence)
print_frequencies(words, frequencies)
