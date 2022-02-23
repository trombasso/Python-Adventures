from functools import lru_cache


def exponent(n):
    if n > 0:
        return 2 * exponent(n - 1)
    else:
        return 1


def sum(n):
    if n > 0:
        return n + sum(n - 1)
    else:
        return 1


@lru_cache(maxsize=32)
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def move_it(n, fra, til, aux):
    if n==1:
        
    

if __name__ = "__main__":

# print(exponent(2))
# print(sum(10))
# print(fibonacci(8))

# for x in range(1, 900):
#     print(x, " ", fibonacci(x))
