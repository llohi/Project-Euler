import time

start = time.time()

def main():
    
    with open("13.txt") as file:
        lines = file.readlines()
    file.close()

    sum = 0

    for line in lines:        
        sum += int(line)

    sum = str(sum)
    print(sum[0:10])

    end = time.time()
    print(f"runtime: {end - start} seconds")

if __name__ == "__main__":
    main()