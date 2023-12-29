"""
primos menores a """
from math import sqrt
import time


def _is_prime(number):
    for i in range(2,int(sqrt(number)+ 1)):
        if number % i == 0:
            return False
    return (True or number == 2) and 1 != number and number !=0

def prime_position(position):
    for i in range(1,position+1):
        if _is_prime(i):
            print(i)
        


if __name__ == '__main__':
    initial = time.time()
    print(prime_position(100))

    final = time.time()
    print(f'The script takes {final - initial} seconds')