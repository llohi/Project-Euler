'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

# create list of primes using sieve of eratosthenes algorithm
def getPrimes(n):

    # create boolean array of True values
    primesBool = [True for i in range(n + 1)]
    p = 2

    while p * p <= n:

        # if prime number, update all multiples to false
        if primesBool[p]:

            for i in range(p * p, n + 1, p):
                primesBool[i] = False
        
        p += 1

    # store all primes in list
    primes = []

    for p in range(2, n + 1):
        if primesBool[p]:
            primes.append(p)

    return primes

  

def main():

    n = int(input("Find nth prime number: "))
    
    primes = getPrimes(1000005) # modify size if not big enough

    print(f"The {n}th prime is {primes[n - 1]}")


if __name__ == "__main__":
    main()