#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argc = len(sys.argv) - 1
if argc == 0:
    print("0 arguments.")
else:
    print("1 argument:" if argc == 1 else "{:d} arguments:".format(argc))
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{:d}: {:s}".format(i, arg))
