'''
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
'''
import time
import math

start = time.time()

def main():

    print(math.factorial(40) / (math.factorial(20) * math.factorial(20)))

    end = time.time()
    print(f"runtime: {end - start} seconds")

if __name__ == "__main__":
    main()