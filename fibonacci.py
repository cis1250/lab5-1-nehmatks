#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def get_input():
    while true:
        try: 
            num_terms = int(input("Enter the number of fibonacci terms you'd like: "))
            if num_terms > 0: 
                break
            else: 
                print("Please enter a positive integer.")
        else: 
            print("Please enter a valid input.")
            

def fibonacci(terms):
    a = 0
    b = 1
    sequence = []
    for x in range(terms):
        sequence.append(a)
        n_term = a + b
        a = b 
        b = n_term

def print_sequence(sequence):
    for item in sequence:
        print(item, end = " ")

get_input()
fibonacci(num_terms)
print_sequence(sequence)
