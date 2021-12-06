#!/usr/bin/env python3
def solve():
    with open('input.txt', 'r') as f:
        prev = -1
        count = 0
        for line in f:
            val = int(line)
            if prev > 0 and val > prev:
                count += 1
            prev = val
        return count

if __name__ == '__main__':
    print(solve())

