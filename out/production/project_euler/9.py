'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
        a**2  +  b**2  =  c**2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def main():

    for i in range(1, 60):
        n = i
        for j in range(n, 60):

            m = j + 1

            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2

            if a + b + c == 1000:
                print(f"{a} + {b} + {c} = {a + b + c}")  # 375 + 200 + 425 = 1000
                print(f"{a} * {b} * {c} = {a * b * c}")  # 375 * 200 * 425 = 31875000


if __name__ == "__main__":
    main()