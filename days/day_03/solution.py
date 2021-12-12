import numpy as np
import pandas as pd

report = pd.Series(np.loadtxt('days/day_03/input.txt', dtype=str))

sums = [report.str[i].astype(int).sum() for i in range(12)]

gamma = "".join('1' if sum > 500 else '0' for sum in sums)

epsilon = "".join('1' if sum < 500 else '0' for sum in sums)

gamma = int(gamma, 2)

epsilon = int(epsilon, 2)

print(gamma, epsilon, gamma * epsilon)

oxygen = report
i = 0

while len(oxygen) > 1:
    ones = oxygen.str[i].astype(int).sum()
    if ones >= len(oxygen) / 2:
        oxygen = oxygen[oxygen.str[i] == '1']
    else:
        oxygen = oxygen[oxygen.str[i] == '0']
    i += 1

oxygen = oxygen.values[0]

co2 = report
i = 0

while len(co2) > 1:
    ones = co2.str[i].astype(int).sum()
    if ones < len(co2) / 2:
        co2 = co2[co2.str[i] == '1']
    else:
        co2 = co2[co2.str[i] == '0']
    i += 1

co2 = co2.values[0]

oxygen = int(oxygen, 2)

co2 = int(co2, 2)

print(oxygen, co2, oxygen * co2)