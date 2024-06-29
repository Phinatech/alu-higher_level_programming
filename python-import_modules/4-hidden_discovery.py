#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allfunc = dir()
    for i in range(0, len(allfunc)):
        if allfunc[1][:2] != "__":
            print("{:s}".format(allfunc[i]))
