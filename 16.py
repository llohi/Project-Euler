import time

start = time.time()

def main():

    sum = 0
    for i in str(pow(2, 1000)):
        sum += int(i)

    print(sum)

    end = time.time()
    print(f"runtime: {end - start} seconds")


if __name__ == "__main__":
    main()