#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count = count + 1
        except IndexError:
            continue
    print("\nnb_print:", count)
    return count

# Example usage
my_list = [1, 2]
x = 2
printed_elements = safe_print_list(my_list, x)

my_list = [1, 2, 3, 4, 5]
x = 5
printed_elements = safe_print_list(my_list, x)

x = 10
printed_elements = safe_print_list(my_list, x)
