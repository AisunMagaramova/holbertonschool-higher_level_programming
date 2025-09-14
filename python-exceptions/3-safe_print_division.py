#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        # Attempt to divide a by b
        result = a / b
    except ZeroDivisionError:
        # Catch division by zero exception
        result = None
    finally:
        # Print the result inside the finally block
        print("Inside result: {}".format(result))
    return result
