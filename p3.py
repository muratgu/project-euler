'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
def isPrime(n):
    for k in range(2, int(pow(n, 0.5))+1):
        if n % k == 0:
            return False
    return True            

n = 600851475143     
print max([x for x in range(2, int(pow(n, 0.5))) if isPrime(x) and n % x == 0])
