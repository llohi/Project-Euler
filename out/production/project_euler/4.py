'''
A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(i, j):

    p = str(i * j)

    for i in range(0, len(p)):
        if p[i] != p[len(p) - 1 - i]:
            return False
    
    return True
    

def main():

    p = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i, j):
                p = max(i * j, p)
    
    print(p)  # 906609

if __name__ == "__main__":
    main()