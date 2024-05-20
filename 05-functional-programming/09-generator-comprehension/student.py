from itertools import count

def is_prime(number):
    return number >= 2 and all(number % k != 0 for k in range(2, number))

def primes():
    return (n for n in count(2) if is_prime(n))
