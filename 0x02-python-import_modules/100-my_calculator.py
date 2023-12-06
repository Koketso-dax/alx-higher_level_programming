#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ != "__main__":
    exit()

argc = len(sys.argv) - 1
argv = sys.argv
if argc != 3:
    print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
    exit(1)
elif argv[2] == '+':
    fn = add
elif argv[2] == '-':
    fn = sub
elif argv[2] == '*':
    fn = mul
elif argv[2] == '/':
    fn = div
else:
    print("Unknown operator. Available operators: +, -, *, and /")
    exit(1)

a = int(argv[1])
b = int(argv[3])
o = argv[2]
x = fn(a, b)
print("{:d} {:s} {:d} = {:d}".format(a, o, b, x))
