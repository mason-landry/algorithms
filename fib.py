def getNthFib(N:int):
    '''This script is my Python implementation of the famous Fibonacci sequence. It is structured as a function that will return the Nth fibonacci number, where N is an input value. If you want the 100th fibonacci number, run the function getNthFib(100)

    Inputs: N - the index of the fibonacci number you want, starting at 0.
    Outputs: Nth Fibonacci number
    '''
    fib = [0,1] # First 2 fibonnaci numbers
    if N < 3:
        return fib[N]

    for i in range(N-1):
        tmp = sum(fib)
        fib[0] = fib[1]
        fib[1] = tmp
    
    return fib[-1]
    
if __name__ == "__main__":
    print(getNthFib(50))