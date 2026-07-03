# 153 = 1**3+5**3+3**3


def is_armstrong(n):
    num = n
    pow = len(str(n))
    total = 0

    while n>0:
        ld = n % 10
        total += ld**pow
        n = n//10

    return total == num

print(is_armstrong(370))


    
