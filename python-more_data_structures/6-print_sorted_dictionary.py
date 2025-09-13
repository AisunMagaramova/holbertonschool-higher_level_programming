#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort the keys of the dictionary and iterate over them
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
