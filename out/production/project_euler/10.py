'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


# calculate the sum of primes under n
def calculateSum(n):

    # create boolean array of True values
    primesBool = [True for i in range(n + 1)]
    p = 2

    while p * p <= n:

        # if prime number, update all multiples to false
        if primesBool[p] == True:

            for i in range(p * p, n + 1, p):
                primesBool[i] = False
        
        p += 1

    # calculate sum of primes under n
    sum = 0

    for p in range(2, n + 1):
        if primesBool[p]:
            sum += p

    return sum

def main():
    
    print(f"The sum of primes under 2 million if {calculateSum(2000000)}")



if __name__ == "__main__":
    main()