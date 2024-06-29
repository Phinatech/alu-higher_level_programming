#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    last_di = number % 10
    print("{}".format(last_di), end='')
    return (last_di)
