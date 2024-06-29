#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    totalint = 0
    for i in range(1, len(argv)):
        totalint += int(argv[i])
    print("{}".format(totalint))
