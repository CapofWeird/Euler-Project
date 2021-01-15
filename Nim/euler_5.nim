#[
EULER PROJECT PROBLEM 5

Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
]#

proc solution(max_num: int): int =
    var num = 0
    var answer = 0
    var passed = true
    while answer == 0:
        passed = true
        num += max_num
        for i in 1..max_num:
            if num mod i != 0:
                passed = false
                break
        if passed:
            answer = num
    return answer

when isMainModule:
    echo solution(20)