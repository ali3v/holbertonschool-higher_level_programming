#!/usr/bin/python3

def uniq_add(my_list=[]):

    total = 0
    number = []

    for i in my_list:
        if i not in number:
            number.append(i)
            total += i

    return total
