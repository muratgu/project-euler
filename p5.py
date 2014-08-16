'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
for k in range (2, 21):
    n = 0
    while True:
      n += 1
      if sum([n % x for x in range(2, k)]) == 0:
          print k-1, n    
          break
