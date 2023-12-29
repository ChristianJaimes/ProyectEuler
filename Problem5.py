"""
2520 is the smallest number that can be divided by each of the numbers from  to  without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time


def is_divisible_in_range(n,range):
    for i in range:
        if n % i != 0 and n != 0:
            return False
    return True

if __name__ == '__main__':
    initial = time.time() #TODO  Improve the time execution the current time is 70 seg
    i = 1
    while True:
        if is_divisible_in_range(i,range(1,21)):
            break
        i += 1

    print(i)
    final = time.time()
    print(f'The script takes {final - initial} seconds')
