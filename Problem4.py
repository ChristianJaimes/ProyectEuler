"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two -digit numbers is .
9009 = 91 * 99
Find the largest palindrome made from the product of two -digit numbers.
"""
import time
def _is_palindrome(number):
    n = str(number)
    return n[::] == n[::-1]

if __name__ == '__main__':
    initial = time.time()
    largest_palindrome = 0
    for i in range (int(1000/2),1000):
        for j in range (100,1000):
            if _is_palindrome(i*j) and largest_palindrome < i*j:
                largest_palindrome = i*j
                a = i
                b = j

    print(f'The largest palindrome made form the product of 3 digit is: {a} x {b} = {largest_palindrome}')
    final = time.time()
    print(f'The script takes {final - initial} seconds')