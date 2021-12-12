import numpy as np
from collections import defaultdict


caves = np.loadtxt('days/day_12/input.txt', delimiter='-', dtype=str)

connections = defaultdict(list)

for cave in caves:
    connections[cave[0]].append(cave[1])
    connections[cave[1]].append(cave[0])

# Part 1 recursive solution
def find_paths_part_1(current_path):
    current_cave = current_path[-1]
    if np.char.islower(current_cave) and current_cave in current_path[:-1]:
            return 0
    if current_path[-1] == 'end':
        return 1
    next_caves = connections[current_path[-1]]
    return np.sum([find_paths_part_1(current_path + [cave]) for cave in next_caves])

# Part 2 recursive solution
def find_paths_part_2(current_path, small_cave_visited):
    current_cave = current_path[-1]
    if np.char.islower(current_cave) and current_cave in current_path[:-1]:
        if current_cave == 'start' or small_cave_visited:
            return 0
        else:
            small_cave_visited = True
    if current_path[-1] == 'end':
        return 1
    next_caves = connections[current_path[-1]]
    return np.sum([find_paths_part_2(current_path + [cave], small_cave_visited) \
                        for cave in next_caves])

paths_part_1 = find_paths_part_1(['start'])
paths_part_2 = find_paths_part_2(['start'], False)

print(paths_part_1)
print(paths_part_2)