import numpy as np

import timeit
    
start = timeit.default_timer()

heights = np.loadtxt('days/day_9/input.txt', dtype=str)
heights = np.asarray([np.asarray([int(c) for c in s]) for s in heights])

heightmap = np.full((102, 102), 10)
heightmap[1:-1, 1:-1] = heights

low_points = []
for i in range(1, len(heightmap) - 1):
    for j in range(1, len(heightmap) - 1):
        if (heightmap[i, j] < heightmap[i-1, j] and
            heightmap[i, j] < heightmap[i+1, j] and
            heightmap[i, j] < heightmap[i, j-1] and
            heightmap[i, j] < heightmap[i, j+1]):
            low_points.append((i, j))

print(sum(heightmap[i, j] + 1 for i, j in low_points))

basins = {low_point: 0 for low_point in low_points}

for i in range(1, len(heightmap) - 1):
    for j in range(1, len(heightmap) - 1):
        if heightmap[i, j] == 9:
            continue
        x, y = i, j
        while (x, y) not in basins:
            descent = min([(heightmap[x+1, y], (x+1, y)),
                           (heightmap[x-1, y], (x-1, y)),
                           (heightmap[x, y+1], (x, y+1)),
                           (heightmap[x, y-1], (x, y-1))])

            x, y = descent[1]
        basins[(x, y)] += 1       

print(np.prod(sorted(basins.values())[-3:]))

stop = timeit.default_timer()

print('Time: ', stop - start)  