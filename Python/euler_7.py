"""
EULER PROJECT PROBLEM 7

10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?

"""
PRIME_LAST_DIGITS = ['1', '3', '7', '9']

def solution(n: int) -> int:
    primes = [2, 3, 5] # List containing found primes
    i = primes[-1] # The number being tested
    while len(primes) < n:
        is_prime = True
        i += 1
        if list(str(i))[-1] not in PRIME_LAST_DIGITS:
            continue
        for prime in primes:
            if (i % prime == 0):
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes[-1]

if __name__ == "__main__":
    print(solution(10001))