'''
What is the value of the first triangle number to have over five hundred divisors?
'''
import math
import time

start = time.time()

def primefactors(n):

    primes = []

    while n % 2 == 0:
        primes.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        
        while n % i == 0:
            primes.append(i)
            n = n / i

    if n > 2:
        primes.append(n)

    divisors = 1
    for p in list(set(primes)):
        divisors *= primes.count(p) + 1

    return divisors

def main():

    num = 3
    i = 3

    primes = primefactors(num)

    while primes < 500:

        num += i
        i += 1
        primes = primefactors(num)

    print(num)
    end = time.time()
    print(f"runtime: {end - start} seconds")

if __name__ == "__main__":
    main()