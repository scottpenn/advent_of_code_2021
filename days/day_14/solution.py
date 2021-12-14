import numpy as np
from collections import Counter

# Load template
template = list(np.loadtxt('days/day_14/input.txt', dtype=str, max_rows=1).item())

# Load rules for pair insertion
rules = np.loadtxt('days/day_14/input.txt', delimiter=' -> ', dtype=str, skiprows=2)
rules = {pair: new for pair, new in rules}

# Keep track of the count of each letter and each pair of letters
letters = Counter(template)
pairs = Counter("".join(template[i:i+2]) for i in range(0, len(template) - 1))

def polymerize(t, rules, letters, pairs):
    for _ in range(t):
        new_pairs = pairs.copy()
        for pair, count in pairs.items():
            new_letter = rules[pair]
            letters[new_letter] += count
            new_pairs[pair[0] + new_letter] += count
            new_pairs[new_letter + pair[1]] += count
            new_pairs[pair] -= count
        pairs = new_pairs
    return letters.most_common()[0][1] - letters.most_common()[-1][1]

print(polymerize(10, rules, letters, pairs))
print(polymerize(40, rules, letters, pairs))