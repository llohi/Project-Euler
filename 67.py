import time

def compute(triangle):
    for i in reversed(range(len(triangle) - 1)):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    return triangle[0][0]

start = time.time()

def main():

    with open("67.txt") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].split()
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])

    print(compute(lines))

    end = time.time()
    print(f"runtime: {end - start} seconds")

if __name__ == "__main__":
    main()