#!/usr/bin/env python3
def solve():
    with open('input.txt', 'r') as f:
        measurements = [int(measurement) for measurement in f]

    count = 0
    for index in range(2, len(measurements)-1):
        if (measurements[index-2] + measurements[index-1] + measurements[index]) < (measurements[index-1] + measurements[index] + measurements[index+1]):
            count += 1
    return count

if __name__ == '__main__':
    print(solve())

