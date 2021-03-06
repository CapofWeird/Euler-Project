"""
EULER PROJECT PROBLEM 2

Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.

"""

def solution(n: int) -> int:
    """
    Once again, a brute force solution.
    I feel like if I'm gonna really get into these
    problems, I'm gonna need to learn some more math.
    """
    i = 0
    temp_i = 0
    fibonacci = 1
    even_total = 0
    while fibonacci <= n:
        temp_i = fibonacci
        fibonacci = fibonacci + i
        i = temp_i
        if fibonacci % 2 == 0:
            even_total += fibonacci
    return even_total        

def calc_e(n: int) -> int:
    """
    Method off the PE forum
    https://projecteuler.net/thread=2#1200
    I've left it the same with minor changes
    """
    x = y = 1
    sum = 0
    while (sum < n):
        sum += (x + y)
        x, y = x + 2 * y, 2 * x + 3 * y
    return sum

if __name__ == "__main__":
    print(solution(4000000))
