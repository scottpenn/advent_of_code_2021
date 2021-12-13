import numpy as np

navigation = np.loadtxt('days/day_10/input.txt', dtype=str)

chunks = {'(' : ')', '[': ']', '{': '}', '<': '>'}

corruption_score = 0
corruption_dict = {')' : 3, ']': 57, '}': 1197, '>': 25137}

completion_dict = {')' : 1, ']': 2, '}': 3, '>': 4}
completion_scores = []

for nav in navigation:
    corrupted = False
    stack = []
    for char in nav:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        else:
            if char != chunks[stack.pop()]:
                corruption_score += corruption_dict[char]
                corrupted = True
                break
    if not corrupted:
        completion_score = 0
        while len(stack) > 0:
            completion_score *= 5
            completion_score += completion_dict[chunks[stack.pop()]]
        completion_scores.append(completion_score)

print(corruption_score)
print(int(np.median(completion_scores)))