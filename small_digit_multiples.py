def f(n):
    i = 1   # Set initial i value
    while True:
        mult = n*i  # Calculate next multiple
        digits = [d for d in str(mult)] # separate digits
        count = 0   # initialize count
        for d in digits:
            if int(d) <= 2:
                count+=1    # Add to count
        if count == len(digits): 
            return mult # returns multiple only if all digits were <= 2
        else: i += 1
        

        



if __name__ == '__main__':
    print(f(2))
