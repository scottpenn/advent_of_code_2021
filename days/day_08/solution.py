import numpy as np

displays = np.loadtxt('days/day_08/input.txt', delimiter=' | ', dtype=str)

displays = np.char.split(displays)
easy_digits = 0
for signals, digits in displays:
    easy_digits += sum(map(lambda l: l in [2, 3, 4, 7], (len(digit) for digit in digits)))

print(easy_digits)

outputs = 0

for signals, digits in displays:
    numbers = [set() for _ in range(10)]
    # Find the easy numbers
    for signal in signals:
        if len(signal) == 2:
            numbers[1] = set(signal)
        elif len(signal) == 3:
            numbers[7] = set(signal)
        elif len(signal) == 4:
            numbers[4] = set(signal)
        elif len(signal) == 7:
            numbers[8] = set(signal)

    # 2, 3 and 5 logic
    five_segments = filter(lambda s: len(s) == 5, signals)
    two_three_five = [set(num) for num in five_segments]
    
    for signal in two_three_five:
        if numbers[1].issubset(signal):
            numbers[3] = signal
        elif len(signal - numbers[4]) == 3:
            numbers[2] = signal
        elif len(signal - numbers[4]) == 2:
            numbers[5] = signal

    # 0, 6 and 9 logic
    six_segments = filter(lambda s: len(s) == 6, signals)
    zero_six_nine = [set(num) for num in six_segments]
    
    for signal in zero_six_nine:
        if numbers[4].issubset(signal):
            numbers[9] = signal
        elif not numbers[1].issubset(signal) :
            numbers[6] = signal
        else:
            numbers[0] = signal

    output = int("".join([str(numbers.index(set(digit))) for digit in digits]))
    outputs += output

print(outputs)

  