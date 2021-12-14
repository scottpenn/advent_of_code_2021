import numpy as np

dots = np.loadtxt('days/day_13/input.txt', delimiter=',', dtype=int, max_rows=743)
folds = np.loadtxt('days/day_13/input.txt', delimiter='=', dtype=str, skiprows=743)

def fold(dots, folds):
    for axis, crease in folds:
        crease = int(crease)
        if axis[-1] == 'x':
            dots[:, 0] = np.where(dots[:, 0] > crease, crease - (dots[:, 0] - crease), dots[:, 0])
        else:
            dots[:, 1] = np.where(dots[:, 1] > crease, crease - (dots[:, 1] - crease), dots[:, 1])
        dots = np.unique(dots, axis=0)
    return dots

dots = fold(dots, folds[:1])

# Part 1
print(len(dots))

dots = fold(dots, folds[1:])

max_x, max_y = np.max(dots, axis=0)

code = np.full((max_y + 1, max_x + 1), ' ')

for x, y in dots:
    code[y, x] = "█"

# Part 2
for row in code:
    print(str.join("", row))