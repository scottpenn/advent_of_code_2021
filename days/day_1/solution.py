import numpy as np

depths = np.loadtxt('days/day_1/input.txt')

increased = 0

for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        increased += 1

print(increased)

increased = 0

for i in range(3, len(depths)):
    if sum(depths[i-2:i+1]) > sum(depths[i-3:i]):
        increased += 1

print(increased)
