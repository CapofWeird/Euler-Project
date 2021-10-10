"""
EULER PROJECT PROBLEM 16

Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def solution(n: int):
    total = 0
    for i in str(2 ** n):
        total += int(i)
    return total


if __name__ == "__main__":
    print(solution(1000))
