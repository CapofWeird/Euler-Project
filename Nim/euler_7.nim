#[
EULER PROJECT PROBLEM 7

10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
]#
const PrimeLastDigits = ['1', '3', '7', '9']

proc solution(n: int): int =
    var allPrimes = @[2, 3, 5]
    var number = allPrimes[high(allPrimes)]
    var strNum: string
    while len(allPrimes) < n:
        number += 1
        strNum = $number
        block primeCheck:
            if PrimeLastDigits.contains(strNum[high(strNum)]):
                for prime in allPrimes:
                    if number mod prime == 0:
                        break primeCheck
                allPrimes.add(number)
    return allPrimes.pop()

when isMainModule:
    echo solution(10001)