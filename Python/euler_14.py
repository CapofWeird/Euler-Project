"""
EULER PROJECT PROBLEM 14

Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def solution(n: int):
    prev_checks = {}
    high_num = 0
    high_term = 0
    for x in range(n):
        seq = []
        term_count = 0
        next_num = x + 1
        if next_num == n:
            break
        while next_num != 0:
            seq.append(next_num)
            if next_num in prev_checks:
                term_count += prev_checks.get(next_num)
                next_num = 0
            else:
                term_count += 1
                if (next_num % 2 == 0):  # even number rule
                    next_num /= 2
                elif next_num == 1:  # escape plan
                    next_num = 0
                else:  # odd number rule
                    next_num = ((next_num * 3) + 1)
        for i in range(len(seq)):
            prev_checks[seq[i]] = term_count - i
        prev_checks[x + 1] = term_count
        if term_count > high_term:
            high_term = term_count
            high_num = x + 1
    return high_num


if __name__ == "__main__":
    print(solution(1000000))
