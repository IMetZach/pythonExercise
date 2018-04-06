#!/bin/python

import sys

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a),
        a, b = b, a+b

numInput = sys.argv

try:
    num = int(numInput[1])
except IndexError:
    print('Usage: fibonacci <number>')
else:
    fib(num)
