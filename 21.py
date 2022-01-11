import time
import math

start = time.time()

def d(n):
    
    sum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum += i
            sum += n / i

    return sum


def main():

    sum = 0

    for i in range(1, 10000):
        n = d(i)
        if n != i:
            if d(n) == i:
                sum += i

    print(sum)

    end = time.time()
    print(f"runtime: {end - start} seconds")

if __name__ == "__main__":
    main()