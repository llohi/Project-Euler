'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def main():

    n = 1
    m = 1

    while m <= 20:

        if n % m == 0:
            m += 1
        
        else:
            print(n)
            for i in range(2, m + 1):
                if (n * i) % m == 0:
                    n *= i
                    m += 1
                    break
    
    print(n)  # 232792560

if __name__ == "__main__":
    main()