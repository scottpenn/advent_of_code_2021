import numpy as np
from collections import defaultdict, Counter
import sys

regex = 'target area: x=(\d*)..(\d*), y=(-*\d*)..(-*\d*)'
target = np.fromregex('days/day_17/input.txt', regex, dtype='int')

x_min, x_max, y_min, y_max = target[0]

# print(x_min, x_max, y_min, y_max)

best_x_velocity = (sys.maxsize, 1)
x_velocities = {}
x_test = 1
while x_test <= x_max:
    x_velocity = x_test
    x = 0
    step = 1
    step_entered = sys.maxsize
    while x_velocity >= 0:
        x += x_velocity
        if x_min <= x <= x_max:
            step_entered = min(step, step_entered)
            x_velocities[x_test] = step_entered
            if x_velocity == 0:
                if step_entered < best_x_velocity[0]:
                    best_x_velocity = (step_entered, x_test)
        x_velocity -= 1
        step += 1
    x_test += 1

# print(x_velocities)
# print(best_x_velocity)

max_y_height = 0
y_test = 0
while y_test < 200:
    step, x_velocity = best_x_velocity
    y_velocity = y_test
    y = 0
    max_y = 0
    for _ in range(1, step):
        y += y_velocity
        max_y = max(y, max_y)
        y_velocity -= 1
    while True:
        if y < y_min:
            break
        y += y_velocity
        max_y = max(y, max_y)
        if y_min <= y <= y_max:
            max_y_height = max(max_y, max_y_height)
            # print(x_velocity, y_test, step, max_y)
            break
        y_velocity -= 1
    y_test += 1

print(max_y_height)

all_velocities = []
y_test = y_min
while y_test < 200:
    for x_test, step in x_velocities.items():
        x_velocity = x_test
        y_velocity = y_test
        x = 0
        y = 0
        while y >= y_min and x <= x_max:
            x += x_velocity
            y += y_velocity
            if x_min <= x <= x_max and y_min <= y <= y_max:
                all_velocities.append((x_test, y_test))
                break
            x_velocity -= 1
            x_velocity = max(x_velocity, 0)
            y_velocity -= 1
    y_test += 1

print(len(set(all_velocities)))