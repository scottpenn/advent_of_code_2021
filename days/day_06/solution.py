import numpy as np
from collections import deque
import timeit

fish = np.loadtxt('days/day_06/input.txt', delimiter=',', dtype=int)

def fesh(days):
    fish_counts = deque(np.zeros(9, dtype=int))

    for f in fish:
        fish_counts[f] += 1

    for _ in range(days):
        fish_counts.rotate(-1)
        fish_counts[6] += fish_counts[8]

    return sum(fish_counts)
    
start = timeit.default_timer()

print(fesh(80))
print(fesh(256))

stop = timeit.default_timer()

print('Time: ', stop - start)  

# start = timeit.default_timer()

# fish_counts = Counter(fish)

# for _ in range(80):
#     fish = fish - 1
#     new_fish = np.count_nonzero(fish == -1)
#     fish = np.append(fish, np.full(new_fish, 8))
#     fish = np.where(fish == -1, 6, fish)

# print(len(fish))

# for _ in range(256):
#     next_fish_counts = Counter()
#     next_fish_counts[8] += fish_counts[0]
#     next_fish_counts[6] += fish_counts[0]
#     for i in range(1, 9):
#         next_fish_counts[i-1] += fish_counts[i]
#     fish_counts = next_fish_counts

# print(sum(fish_counts.values()))

# stop = timeit.default_timer()

# print('Time: ', stop - start) 