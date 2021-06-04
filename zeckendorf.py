import math
import itertools

def getAllFibs(n):
    '''Find all fibonacci numbers up to n'''
    fib_sum = [1,2]
    while True:
        test = fib_sum[-1] + fib_sum[-2]
        if test < n:
            fib_sum.append(test)
        else:
            break
    return fib_sum
    

def f(n):
    '''f(n) is the number of ways we can represent an integer n>=0 as the sum of different fibonacci numbers.

    f(16) should be 4
    f(100) should be 415

    find f(10^13)
    '''
    ## Find highest fibonacci number that is less than n
    fibs = getAllFibs(n)
    ## Check every combination of fibs to see if it sums up to n, avoiding repeats
    combis = []
    count = 0
    

    for i in range(0, len(fibs)+1):
        tmp_combis = list(itertools.combinations(fibs,i))
        for c in tmp_combis:
            combis.append(tuple(set(c)))
    combis = list(set(combis))
    
    for c in combis:
        if sum(c) == n:
            print("Sum of ",c,"=",n)
            count += 1
    return count

def S(n):
    ''' returns sum of all k=0 through n of f(k)'''
    s = 0
    for k in range(n+1):
        print(n,k,f(k))
        s += f(k)
    return s
if __name__ == "__main__":
    print(S(10000))
    # print(getAllFibs(17))
    # print(f(100))