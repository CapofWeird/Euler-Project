"""
EULER PROJECT PROBLEM 3

Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def solution(n: int) -> int:
    prime_factors = []
    next_factor = 2
    while True:
        if n % next_factor == 0:
            prime_factors.append(next_factor)
            n /= next_factor
        else:
            if next_factor >= n:
                break
            next_factor += 1
    return prime_factors[-1]

if __name__ == "__main__":
    print(solution(600851475143))
