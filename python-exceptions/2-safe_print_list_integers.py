#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Check if the current element is an integer
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            # If x is larger than the length of my_list, break the loop
            break
    print()  # To print the newline after the output
    return count
