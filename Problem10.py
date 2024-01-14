"""
The sum of the primes below 10 is 2 + 5 7 =17.
Find the sum of all the primes below two million.
"""

from math import sqrt
import time

def _is_prime(number):
    for i in range(2,int(sqrt(number)+ 1)):
        if number % i == 0:
            return False
    return (True or number == 2) and 1 != number and number !=0

def sum_primes_under_the_value(value):
    sum = 0
    for i in range(0,value + 1):
        if _is_prime(i):
            sum += i
    return sum

if __name__ == '__main__':
    initial = time.time()

    n = 2000000
    sum = sum_primes_under_the_value(n)
    
    print(f'sum = {sum}')

    final = time.time()
    print(f'The script takes {final - initial} seconds')



