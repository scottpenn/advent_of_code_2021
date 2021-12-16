import numpy as np
from collections import defaultdict, Counter
import sys

transmission = np.loadtxt('days/day_16/input.txt', dtype=str).item()
transmission = "".join([f'{int(c, 16):04b}' for c in transmission])

def read_packet(c):
    packet_version = int(transmission[c:c+3], 2)
    # print(transmission[c:c+3], packet_version)
    version_numbers.append(packet_version)
    c += 3

    packet_type = int(transmission[c:c+3], 2)
    # print(transmission[c:c+3], packet_type)
    c += 3

    match packet_type:
        case 4:
            literal = ''
            while transmission[c] != '0':
                c += 1
                literal += transmission[c:c+4]
                c += 4
            c += 1
            literal += transmission[c:c+4]
            c += 4
            value = int(literal, 2)
        case _:
            length_type = transmission[c]
            c += 1

            values = []
            match length_type:
                case '0':
                    length = int(transmission[c:c+15], 2)
                    c += 15
                    limit = c + length
                    while c < limit:
                        c, val = read_packet(c)
                        values.append(val)
                case '1':
                    length = int(transmission[c:c+11], 2)
                    c += 11
                    for _ in range(length):
                        c, val = read_packet(c)
                        values.append(val)
            match packet_type:
                case 0:
                    value = np.sum(values)
                case 1:
                    value = np.prod(values)
                case 2:
                    value = np.min(values)
                case 3:
                    value = np.max(values)
                case 5:
                    value = values[0] > values[1]
                case 6:
                    value = values[0] < values[1]
                case 7:
                    value = values[0] == values[1]           
    return c, value

version_numbers = []
# cursor
c = 0

_, val = read_packet(c)

print(sum(version_numbers))
print(val)