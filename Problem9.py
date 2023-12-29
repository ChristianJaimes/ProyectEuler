"""
A Pythagorean triplet is a set of three natural numbers,a < b < c, for which,

For example,
 a^2 + b^2 = c^2
 3^2 + 4^2 = 5^2
 9   +  16 = 25

There exists exactly one Pythagorean triplet for which a + b + c = 1000
Find the product . a x b x c
"""

def _is_pythagorean_triplet(a,b,c):
    if  a < b and b < c:
        if a**2 + b**2 == c**2:
            return True
    return False
    

if __name__ == '__main__':
    print(_is_pythagorean_triplet(4,5,6))
    i = 1
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            for c in range(b + 1, 1000):
                if a + b + c == 1000 :
                    if _is_pythagorean_triplet(a,b,c):
                        print(f'{a} + {b} + {c} = 1000, and axbxc = {a*b*c}')
                    