"""
By listing the first six prime numbers: 2,3,5,7,11 and 13 we can see that the 6th prime is 13.

What is the st prime number 10 001?"""
from math import sqrt
import time


def _is_prime(number):
    for i in range(2,int(sqrt(number)+ 1)):
        if number % i == 0:
            return False
    return (True or number == 2) and 1 != number and number !=0

def prime_position(position):
    counter = 1
    i = 1
    while counter <= position:
        if _is_prime(i):
            print(f'{counter}: {i}')
            counter += 1
        i += 1
    return i-1
        


if __name__ == '__main__':
    initial = time.time()
    print(prime_position(10001))

    final = time.time()
    print(f'The script takes {final - initial} seconds')