import numpy as np

movements = np.loadtxt('days/day_02/input.txt', dtype=str)

horizontal = 0
depth = 0

for movement, value in movements:
    value = int(value)
    if movement == 'forward':
        horizontal += value
    elif movement == 'down':
        depth += value
    else:
        depth -= value

print(horizontal * depth)

horizontal = 0
depth = 0
aim = 0

for movement, value in movements:
    value = int(value)
    if movement == 'forward':
        horizontal += value
        depth += aim * value
    elif movement == 'down':
        aim += value
    else:
        aim -= value

print(horizontal * depth)
