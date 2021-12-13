import numpy as np

crabs = np.loadtxt('days/day_07/input.txt', delimiter=',', dtype=int)

min_fuel = np.sum(np.abs(crabs - 1))

for i in range(2, np.max(crabs)):
    fuel = np.sum(np.abs(crabs - i))
    min_fuel = np.min([fuel, min_fuel])

print(min_fuel)

min_fuel = np.sum((np.abs(crabs - 1) * (np.abs(crabs - 1) + 1)) // 2 )

for i in range(2, np.max(crabs)):
    n = np.abs(crabs - i)
    fuel = np.sum(n * (n + 1) // 2)
    min_fuel = np.min([fuel, min_fuel])

print(min_fuel)

  