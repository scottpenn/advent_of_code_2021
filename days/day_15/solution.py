import numpy as np
from collections import defaultdict
import sys
import heapq

risk_levels = np.loadtxt('days/day_15/input.txt', dtype=str)
risk_levels = np.asarray([np.asarray([int(c) for c in s]) for s in risk_levels])

def find_best_path(risk_levels):
    risk_levels = np.pad(risk_levels, 1, constant_values=10)
    max_x, max_y = risk_levels.shape[0] - 2, risk_levels.shape[1] - 2

    best_paths = defaultdict(lambda: sys.maxsize)
    best_paths[(1, 1)] = 0

    unvisited = []
    heapq.heappush(unvisited, (best_paths[(1, 1)], (1, 1)))

    visited = set()

    while unvisited:
        risk, node = heapq.heappop(unvisited)
        if risk != best_paths[node]:
            continue
        x, y = node
        for adjacent_node in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            # Avoid padded edge of grid
            if risk_levels[adjacent_node] > 9:
                visited.add(adjacent_node)
            if adjacent_node not in visited:
                risk = best_paths[node] + risk_levels[adjacent_node]
                if risk < best_paths[adjacent_node]:
                    best_paths[adjacent_node] = risk
                    heapq.heappush(unvisited, (risk, adjacent_node))
        visited.add(node)

    return best_paths[(max_x, max_y)]

print(find_best_path(risk_levels))

risk_levels_extended = np.zeros((risk_levels.shape[0] * 5, risk_levels.shape[1] * 5), dtype=int)

size = risk_levels.shape[0]
for x in range(500):
    for y in range(500):
        original = risk_levels[x % size, y % size]
        modifier = x // size + y // size
        risk_levels_extended[x, y] = ((original + modifier - 1) % 9) + 1

print(find_best_path(risk_levels_extended))

# Slow DFS Solution with Pruning (2.5s runtime for Part 1)

# nodes_considered = [0]
# def find_best_path(risk_levels, current_position, total_risk):
#     nodes_considered[0] += 1

#     max_x, max_y = risk_levels.shape[0] - 1, risk_levels.shape[1] - 1

#     # Reached the end
#     if current_position == (max_x, max_y):
#         print(best_paths[(max_x, max_y)], nodes_considered[0], total_risk)
#         return

#     x, y = current_position
#     moves = []
#     # Can Move Right
#     if y < max_y:
#         right = (x, y + 1)
#         if total_risk + risk_levels[right] < best_paths[right]:
#             moves.append((risk_levels[right], risk_levels[right], right))
#     # Can Move Down
#     if x < max_x:
#         down = (x + 1, y)
#         if total_risk + risk_levels[down] < best_paths[down]:
#             moves.append((risk_levels[down], risk_levels[down], down))

#     # Can Move Left
#     if y > 0:
#         left = (x, y - 1)
#         if total_risk + risk_levels[left] < best_paths[left]:
#             moves.append((risk_levels[left] + 8, risk_levels[left], left))
#     # Can Move Up
#     if x > 0:
#         up = (x - 1, y)
#         if total_risk + risk_levels[up] < best_paths[up]:
#             moves.append((risk_levels[up] + 8, risk_levels[up], up))

#     # print(moves)
#     for _, risk, node in sorted(moves):
#         node_x, node_y = node
#         if ((new_total_risk := total_risk + risk) +
#                 (max_x - node_x) +
#                 (max_y - node_y)) < best_paths[(max_x, max_y)]:
#             best_paths[node] = new_total_risk
#             find_best_path(risk_levels, node, new_total_risk)
#     return

# find_best_path(risk_levels, (0, 0), 0)
# print(best_paths[(risk_levels.shape[0] - 1, risk_levels.shape[1] - 1)])
# print(nodes_considered[0])