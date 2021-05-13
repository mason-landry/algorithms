def factorial(n:int):
    if n == 1:
        return 1
    else:
        return n* factorial(n-1)

def tail_factorial(n:int, total=1):
    if n==1:
        return total
    else:
        return tail_factorial(n-1,total*n)

if __name__ == '__main__':
    print(factorial(24))
    print(tail_factorial(24))