import numpy as np

lines = np.loadtxt('days/day_05/input.txt', delimiter=' -> ', dtype=str)

lines = np.char.split(lines, ',')

grid = np.zeros((1000, 1000), dtype=int)

for line in lines:
    x1, y1 = int(line[0][0]), int(line[0][1])
    x2, y2 = int(line[1][0]), int(line[1][1])

    if x1 == x2:
        y1, y2 = sorted([y1, y2])
        for y in range(y1, y2 + 1):
            grid[x1, y] += 1
    elif y1 == y2:
        x1, x2 = sorted([x1, x2])
        for x in range(x1, x2 + 1):
            grid[x, y1] += 1
    else:
        (x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])
        for i in range(x2 - x1 + 1):
            if y2 > y1:
                grid[x1 + i, y1 + i] += 1
            else:
                grid[x1 + i, y1 - i] += 1

print(np.count_nonzero(grid >= 2))
