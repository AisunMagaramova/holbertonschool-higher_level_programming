#!/usr/bin/python3
#!/usr/bin/python3
safe_print_list_integers = __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4]
x = len(my_list) + 4  # Bu testdə x 8 olacaq, amma listin uzunluğu 4dür

nb_print = safe_print_list_integers(my_list, x)
print("nb_print: {:d}".format(nb_print))
