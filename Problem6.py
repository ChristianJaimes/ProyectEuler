"""
"""
import time


def _sum_of_squares(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2

    return sum

def _square_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum**2

def sum_of_squares_and_square_of_sum(n):
    sum_of_squares = 0
    sum = 0
    for i in range(1,n+1):
        sum_of_squares += i ** 2
        sum += i
    square_sum = sum ** 2
    return square_sum, sum_of_squares


if __name__ == '__main__':
    initial = time.time()
    square_sum, sum_of_squares = sum_of_squares_and_square_of_sum(100)
    print(f'{square_sum} - {sum_of_squares} = {square_sum - sum_of_squares}')
    final = time.time()
    print(f'The script takes {final - initial} seconds')