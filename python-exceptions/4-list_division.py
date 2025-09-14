#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Check if the lists are long enough to access the current index
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]

            # Check if both elements are either integers or floats
            if isinstance(element_1, (int, float)) and isinstance(element_2, (int, float)):
                # Perform division
                result.append(element_1 / element_2)
            else:
                result.append(0)
                print("wrong type")
        except ZeroDivisionError:
            # Handle division by zero error
            result.append(0)
            print("division by 0")
        except IndexError:
            # Handle out of range error
            result.append(0)
            print("out of range")
        except Exception as e:
            # Catch any other unforeseen errors and handle them gracefully
            result.append(0)
            # Split the error message to avoid exceeding 79 characters
            print("Error: " + str(e))  # Breaking the message into smaller parts

    return result
