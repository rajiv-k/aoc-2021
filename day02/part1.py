#!/usr/bin/env python3
def solve():
    with open('input.txt', 'r') as f:
        horizontal, depth = 0, 0
        for line in f:
            direction, val = line.split()
            if direction == "forward":
                horizontal += int(val)
            elif direction == "down":
                depth += int(val)
            elif direction == "up":
                depth -= int(val)
            else:
                print("invalid input")

        return horizontal*depth

if __name__ == '__main__':
    print(solve())

