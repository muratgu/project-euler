'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
'''
def isPrime(n):
    if n < 2:
        return False
    for k in range(2, int(pow(n, 0.5))+1):
        if n % k == 0:
            return False
    return True     
    
k = 0
i = 1
max = 10001
while True:
    i += 1
    if isPrime(i):
        k += 1
        if k >= max:
            print i
            break 