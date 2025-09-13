#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Convert the list to a set to remove duplicates, then sum the unique values
    return sum(set(my_list))
