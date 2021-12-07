#!/usr/bin/env python3
def solve():
    with open('input.txt', 'r') as f:
        horizontal, depth = 0, 0
        aim = 0
        for line in f:
            direction, _val = line.split()
            val = int(_val)
            if direction == "forward":
                horizontal += val
                depth += (aim * val)
            elif direction == "down":
                aim += val
            elif direction == "up":
                aim -= val
            else:
                print("invalid input")

        return horizontal*depth

if __name__ == '__main__':
    print(solve())

