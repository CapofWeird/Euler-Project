#[
EULER PROJECT PROBLEM 4

Largest palindrome product

A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
]#

proc palindromic(number: int): bool =
    let strNum = $number
    var isPalindromic = true
    for i in 1..len(strNum):
        if strNum[i - 1] != strNum[high(strNum) - i + 1]:
            isPalindromic = false
            break
    return isPalindromic

proc solution(digits: int): int =
    var baseDigit = 9
    for i in 1..<digits:
        baseDigit = (baseDigit * 10) + 9
    var num1, num2 = baseDigit
    var highest = 0
    var checkNum: int
    while num1 > (baseDigit div 10):
        checkNum = num1 * num2
        if palindromic(checkNum):
            if checkNum > highest:
                highest = checkNum
        num2 -= 1
        if num2 <= (baseDigit div 10):
            num1 -= 1
            num2 = baseDigit
    return highest

when isMainModule:
    echo solution(3)