#[
EULER PROJECT PROBLEM 3

Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
]#

proc solution(m: int64): int =
    var prime_factors = newSeq[int]()
    var next_factor = 2
    var n = m
    while true:
        if n mod next_factor == 0:
            prime_factors.add(next_factor)
            n = n div next_factor
        else:
            if next_factor >= n:
                break
            next_factor += 1
    return prime_factors[high(prime_factors)]

when isMainModule:
    echo solution(600851475143)