'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
def isPrime(n):
    for k in range(2, int(pow(n, 0.5))+1):
        if n % k == 0:
            return False
    return True 

print sum([x for x in range(2, 10) if isPrime(x)])
print sum([x for x in range(2, 2000000) if isPrime(x)])
        