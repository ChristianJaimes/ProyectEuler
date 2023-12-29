import time

def fibonacci_iterative(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

def sup_evens_optimized(limit):
    sum_even = 0
    i = 0
    while True:
        fib = fibonacci_iterative(i)
        if fib > limit:
            break
        if fib % 2 == 0:
            sum_even += fib
        i += 1
    print(f'The sum of even-valued terms is: {sum_even}')

if __name__ == '__main__':
    initial = time.time()
    sup_evens_optimized(4000000)
    final = time.time()
    print(f'The script takes {final - initial} seconds')
