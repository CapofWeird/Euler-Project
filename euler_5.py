"""
EULER PROJECT PROBLEM 5

Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?

"""
# This solution works, but it took a few minutes
# so there's probably a more efficient method
def solution(max_num: int) -> int:
    next_num = 0
    answer = 0
    while answer == 0:
        next_num += 1
        i = 0
        for x in range(max_num):
            if (next_num % (x + 1) == 0):
                i-=-1
            else:
                break
        if (i == max_num):
            answer = next_num
    return answer

if __name__ == "__main__":
    print(solution(20))