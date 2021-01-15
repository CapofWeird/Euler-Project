#[
EULER PROJECT PROBLEM 6

Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of
the first ten natural numbers and the square of the sum is,
3025 - 385 = 2640

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.
]#
import math

proc solution(max_num: int): int =
    var square_sum = 0
    var sum_square = 0
    for i in 1..max_num:
        square_sum += i
        sum_square += i^2
    return square_sum^2 - sum_square

when isMainModule:
    echo solution(100)
