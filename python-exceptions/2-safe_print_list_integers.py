#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Çap edirik yalnız integer-ləri
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            # Əgər x uzunluqdan böyükdürsə, traceback çap et
            print("\nTraceback (most recent call last):")
            print(f"  File \"{__file__}\", line {i+1}, in <module>")
            print("IndexError: list index out of range")
            break
    print()  # Sətir sonu
    return count
