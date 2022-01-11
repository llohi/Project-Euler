'''
By considering the terms in the Fibonacci sequence
whose  values do not exceed four million, find the
sum of the even-valued terms.
'''

def main():

    #  generate list of fibonacci numbers
    fibs = [1, 2]
    current = 1
    next = 2
    while current + next <= 4000000:
        new = current + next
        fibs.append(new)

        current = next
        next = new

    #  calculate sum of even-valued terms
    sum = 0
    for num in fibs:
        if num % 2 == 0:
            sum += num

    print(f"sum of even-valued terms = {sum}\n")  # 4613732

if __name__ == "__main__":
    main()
