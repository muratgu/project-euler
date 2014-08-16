'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
'''
def fib(n):
    '''
    Binet's formula for nth Fibonacci number
    http://mathworld.wolfram.com/BinetsFibonacciNumberFormula.html
    ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))    
    '''
    return int(0.4472135954999579392818347337462552470881236719223051448541*
    (pow(1.6180339887498948482045868343656381177203091798057628621354,n) - 
    pow(-0.618033988749894848204586834365638117720309179805762862135,n)))
    
total = 0
max = 4000000
for k in range(2, max):
    x = fib(k)
    if x > max:
        break
    if x % 2 == 0:
        total += x
print total
