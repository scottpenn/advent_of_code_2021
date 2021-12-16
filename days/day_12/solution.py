import numpy as np
from collections import defaultdict

caves = np.loadtxt('days/day_12/input.txt', delimiter='-', dtype=str)

connections = defaultdict(list)

for cave in caves:
    connections[cave[0]].append(cave[1])
    connections[cave[1]].append(cave[0])

# Part 1 recursive solution
def find_paths_part_1(current_path, current_cave):
    total_paths = 0
    next_caves = connections[current_cave]
    for cave in next_caves:
        if cave == 'end':
            total_paths += 1
        elif cave in current_path and np.char.islower(cave):
            continue
        else:
            total_paths += find_paths_part_1(set(current_path | {cave}), cave)
    return total_paths

# Part 2 recursive solution
def find_paths_part_2(current_path, current_cave, small_cave_visited):
    total_paths = 0
    next_caves = connections[current_cave]
    for cave in next_caves:
        if cave == 'end':
            total_paths += 1
        elif cave == 'start':
            continue
        elif cave in current_path and np.char.islower(cave):
            if small_cave_visited:
                continue
            else:
                total_paths += find_paths_part_2(current_path, cave, True)
        else:
            total_paths += find_paths_part_2(set(current_path | {cave}), cave, small_cave_visited)
    return total_paths

paths_part_1 = find_paths_part_1({'start'}, 'start')
paths_part_2 = find_paths_part_2({'start'}, 'start', False)

print(paths_part_1)
print(paths_part_2)