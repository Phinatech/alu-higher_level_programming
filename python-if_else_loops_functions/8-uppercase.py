#!/usr/bin/python3
def uppercase(str):
    for itea in str:
        temp = itea
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(itea) - 32)
        print("{}".format(temp), end='')
    print()
