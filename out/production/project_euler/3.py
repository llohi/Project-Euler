'''
The prime factors of 13195 are 5, 7, 13 and 29. What is
the largest prime factor of the number 600851475143?
'''

def main():

	n = 600851475143
	f = 1
	i = 1
	while n != 1:

		if n % (6 * i - 1) == 0:
			f = 6 * i - 1
			n /= f

		if n % (6 * i + 1) == 0:
			f = 6 * i + 1
			n /= f

		i += 1

	print(f)  # 6857


if __name__ == "__main__":
    main()
