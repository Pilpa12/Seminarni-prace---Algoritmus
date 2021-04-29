from math import sqrt, floor


def getprimes(numbers):
    primes = []
    for number in numbers:
        if number > 1:
            divisors = []  # seznam dělitelů
            maxdivisor = floor(
                sqrt(number)
            )  # horní hranice čísel, kterými budeme zkoušet dělit zadané číslo
            for i in range(2, maxdivisor+1):
                if number % i == 0:
                    divisors.append(i)

            if len(divisors) == 0:
                primes.append(number)

    return sorted(primes)
