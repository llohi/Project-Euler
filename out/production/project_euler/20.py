# Find the sum of the digits in the number 100!

import time

start = time.time()

def main():

    n = 1
    for i in range(1, 101):
        n *= i

    n = str(n)

    sum = 0
    for c in n:
        sum += int(c)

    print(sum)

    end = time.time()
    print(f"runtime: {end - start} seconds")

if __name__ == "__main__":
    main()