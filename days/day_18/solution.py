import numpy as np
from collections import defaultdict, Counter
import sys


numbers = np.loadtxt('days/day_18/input.txt', delimiter='\n', dtype='str')
# print(numbers)

def read_number(line):
    numbers = []
    depth = 0
    for c in line:
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
        elif c == ',':
            pass
        else:
            numbers.append((depth, int(c)))
    return numbers

def add_numbers(n1, n2):
    number = n1 + n2
    number = [(depth + 1, n) for depth, n in number]
    return number

def reduce_number(n):
    if np.any(depth >= 5 for depth, _ in n):
        n = explode_number(n)
    while True:
        n, did_split = split_number(n)
        if not did_split:
            break
        if np.any(depth >= 5 for depth, _ in n):
            n = reduce_number(n)
    return n

def explode_number(n):
    i = 0
    # Explode
    while i < len(n) - 1:
        if n[i][0] >= 5:
            # print("Explode!")
            if i > 0:
                n[i - 1] = (n[i - 1][0], n[i][1] + n[i - 1][1])
            n.pop(i)
            if i < len(n) - 1:
                n[i + 1] = (n[i + 1][0], n[i][1] + n[i + 1][1])
            n[i] = (n[i][0] - 1, 0)
            i -= 1
            # print(n)
        i += 1
    return n

def split_number(n):
    i = 0
    did_split = False
    # Split
    while i < len(n):
        if n[i][1] > 9:
            # print("Split!")
            n.insert(i + 1, (n[i][0] + 1, int(np.ceil(n[i][1] / 2))))
            n[i] = (n[i][0] + 1, n[i][1] // 2)
            did_split = True
            break
        i += 1
    return n, did_split

def magnitude(n):
    i = 0
    while len(n) > 1 and i < len(n) - 1:
        if n[i][0] == n[i + 1][0]:
            n[i] = (n[i][0] - 1, n[i][1] * 3 + n[i + 1][1] * 2)
            n.pop(i + 1)
            i = max(0, i - 1)
        else:
            i += 1

    return n[0][1]
        
number = read_number(numbers[0])

for line in numbers[1:]:
    next_number = read_number(line)
    number = add_numbers(number, next_number)
    number = reduce_number(number)

# print(number)

print(magnitude(number))

magnitudes = {}
for x in range(len(numbers)):
    for y in range(len(numbers)):
        if x != y and (x, y) not in magnitudes:
            n1 = read_number(numbers[x])
            n2 = read_number(numbers[y])
            number = add_numbers(n1, n2)
            number = reduce_number(number)
            magnitudes[(x, y)] = magnitude(number)

print(max(magnitudes.values()))