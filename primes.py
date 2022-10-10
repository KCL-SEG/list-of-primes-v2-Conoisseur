"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError

    list = []
    list.append(2)

    for i in range(number_of_primes - 1):
        numberToCheck = list[-1] + 1
        while not isPrime(numberToCheck):
            numberToCheck += 1
        list.append(numberToCheck)

    return list


def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
