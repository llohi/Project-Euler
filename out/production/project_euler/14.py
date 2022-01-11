import time

start = time.time()


def main():

    n = 1
    max = 0
    max_n = 1
    paths = []

    while n < 1000000:

        collatz = 1
        i = n
        while i > 1:

            if i % 2 == 0:
                i = i / 2
            else:
                i = 3 * i + 1

            if i < n:
                collatz += paths[int(i - 1)]
                break

            collatz += 1

        if collatz > max:
            max = collatz
            max_n = n

        paths.append(collatz)
        n += 1

    print(f"longest chain: {max} with {max_n}")

    end = time.time()
    print(f"runtime: {end - start} seconds")

if __name__ == "__main__":
    main()