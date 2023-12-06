#!/usr/bin/python3
import sys
import hidden_4 as hd

if __name__ != "__main__":
    exit()

for name in dir(hd):
    if name[:2] != "__":
        print(name)
