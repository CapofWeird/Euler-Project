"""
EULER PROJECT PROBLEM 4

Largest palindrome product

A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
def palindromic(num: int) -> bool:
    is_palindrome = True
    num = list(str(num))
    for x in range(len(num)):
        if num[x] != num[len(num) - (x + 1)]:
            is_palindrome = False
            break
    return is_palindrome

def solution(digits: int) -> int:
    num1 = num2 = 9 * (int('1' * digits))
    palindromes = []
    while num1 > (9 * (int('1' * (digits - 1)))):
        check_num = num1 * num2
        if palindromic(check_num) == True:
            palindromes.append(check_num)
        num2 -= 1
        if num2 <= (9 * (int('1' * (digits - 1)))):
            num1 -= 1
            num2 = 9 * (int('1' * digits))
    palindromes.sort(reverse=True)
    return palindromes[0]

if __name__ == "__main__":
    print(solution(4))