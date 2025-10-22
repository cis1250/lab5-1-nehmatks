#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)


def get_input(num_terms):
    while True:
        try: 
            num_terms = int(input("Enter the number of fibonacci terms you'd like: "))
            if num_terms > 0: 
                return(num_terms)
            else: 
                print("Please enter a positive integer.")
        except: 
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
    return (sequence)

def print_sequence(sequence):
    for item in sequence:
        print(item, end = " ")
    print("")

num_terms = 0
sequence = []

terms = get_input(num_terms)
sequence = fibonacci(terms)
print_sequence(sequence)
