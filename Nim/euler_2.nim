#[
EULER PROJECT PROBLEM 2

Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
]#

proc solution(n: int): int =
    var i = 0
    var j = 0
    var fibonacci = 1
    var even_total = 0
    while fibonacci <= n:
        j = fibonacci
        fibonacci = fibonacci + i
        i = j
        if fibonacci mod 2 == 0:
            even_total += fibonacci
    return even_total

when isMainModule:
    echo solution(4000000)