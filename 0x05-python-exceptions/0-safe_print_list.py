#!/usr/bin/bash/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if count < x:
                print(i, end="")
                count += 1
            else:
                break
    except:
        pass
    finally:
        print("\nnb_print:", count)
    return (count)

my_list = [1, 2, 3, 4, 5]
x = 2
printed_elements = safe_print_list(my_list, x)
print("Number of elements printed:", printed_elements)

printed_elements = safe_print_list(my_list, 5)
print("Number of elements printed:", printed_elements)

printed_elements = safe_print_list(my_list, 10)
print("Number of elements printed:", printed_elements)
