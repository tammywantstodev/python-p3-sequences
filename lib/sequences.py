#!/usr/bin/env python3



def print_fibonacci(length):
    if length==0:
        print([])
    elif length==1:
        print([0])
    else:
        list_of_numbers=[0,1]
        for _ in range(length-2):
            next_number= list_of_numbers[-1]+list_of_numbers[-2]
            list_of_numbers.append(next_number)
        print(list_of_numbers)
print_fibonacci(0)
#[]
print_fibonacci(1)
#0
