import time
import string

start = time.time()

def main():

    with open("names.txt") as file:
        data = file.read()

    file.close()

    chars = string.ascii_uppercase

    data = data[1:-1]
    data = data.split('","')
    data.sort()
    
    sum = 0
    for i in range(0, len(data)):
        score = 0
        for c in data[i]:
            score += chars.find(c) + 1

        score *= i + 1
        sum += score

    print(sum)

    end = time.time()
    print(f"runtime: {end - start} seconds")

if __name__ == "__main__":
    main()