'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
def isPalindrome(n):
    s = str(n)
    return s == s[::-1]

max = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        k = x*y
        if isPalindrome(k) and k > max:
            max = k
print max                
