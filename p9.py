'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
def isPythagorean(a, b, c):
    return c > b and b > a and (a*a + b*b == c*c)

max = 500 
for i in range(1, max):
   for j in range(i+1, max):
      for k in range(j+1, max): 
         if isPythagorean(i, j, k):
             print i, j, k
             if i+j+k == 1000:
                 print i*j*k
                 exit()            
         