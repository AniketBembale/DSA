# Approach 1 -  Brute Force

def factors(n):
    result = []

    for i in range(1,n+1):
        if n%i==0:
            result.append(i)
    return result

print(factors(20))


# Approach - 2 small Optimization

def factors(n):
    result = []

    for i in range(1,n//2+1):
        if n%i==0:
            result.append(i)
    result.append(n)
    return result

print(factors(20))


# Approach - 3 Optimized  

from math import sqrt

def factors(n):
    result = []

    for i in range(1,int(sqrt(n)+1)):

        if n%i==0:
            result.append(i)
            if n//i != i:
                result.append(n//i) 
    result.sort()
              
    return result

print(factors(20))
