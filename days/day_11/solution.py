import numpy as np
import timeit

octopodes = np.loadtxt('days/day_11/input.txt', dtype=str)
octopodes = np.asarray([np.asarray([int(c) for c in s]) for s in octopodes])
octopodes = np.pad(octopodes, 1)

start = timeit.default_timer()

flashes = 0
for i in range(1000):
    # Part 1 answer
    if i == 100:
        print(flashes)

    # Part 2 answer
    if np.all(octopodes[1:-1, 1:-1] == 0):
        print(i)
        break

    octopodes = octopodes + 1

    while np.any(octopodes[1:-1, 1:-1] > 9):
        # Find all flashing octopodes
        flashers = np.where(octopodes[1:-1, 1:-1] > 9)

        # Keep count of total flashes
        flashes += len(flashers[0])

        # Return energy level back to zero
        octopodes = np.where(octopodes > 9, 0, octopodes)

        # Add 1 to flash-adjacent octopodes
        for x, y in zip(flashers[0] + 1, flashers[1] + 1):
            octopodes[x-1, y-1] += 1 if octopodes[x-1, y-1] > 0 else 0
            octopodes[x, y-1] += 1 if octopodes[x, y-1] > 0 else 0
            octopodes[x+1, y-1] += 1 if octopodes[x+1, y-1] > 0 else 0
            octopodes[x-1, y] += 1 if octopodes[x-1, y] > 0 else 0
            octopodes[x+1, y] += 1 if octopodes[x+1, y] > 0 else 0
            octopodes[x-1, y+1] += 1 if octopodes[x-1, y+1] > 0 else 0
            octopodes[x, y+1] += 1 if octopodes[x, y+1] > 0 else 0
            octopodes[x+1, y+1] += 1 if octopodes[x+1, y+1] > 0 else 0

stop = timeit.default_timer()

print('Time: ', stop - start)  