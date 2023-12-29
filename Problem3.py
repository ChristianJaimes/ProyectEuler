"""
The prime factors of  13195 are  5,7,13 and  29.

What is the largest prime factor of the number  600851475143?
"""

from math import sqrt
import time


def _is_prime(number):
    for i in range(3,int(sqrt(number)+ 1),2):
        if number % i == 0:
            return False
    return (True or number == 2) and 1 != number

def largest_prime_factor(number):
    largest_prime = 2
    while number % 2 == 0:
        number = number / 2
    
    for i in range(3,int(sqrt(number)+ 1),2):
        while number % i == 0:
            largest_prime = i
            number = number / i
    return largest_prime


    


if __name__ == '__main__':
    initial = time.time()
    print(largest_prime_factor(600851475143))
    final = time.time()
    print(f'The script takes {final - initial} seconds')
    