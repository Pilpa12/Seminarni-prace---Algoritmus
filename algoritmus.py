from math import sqrt, floor


def getprimes(numbers):
    primes = []
    for number in numbers:
        if number > 3:
            maxdivisor = floor(
                sqrt(number)
            )  # horní hranice čísel, kterými budeme zkoušet dělit zadané číslo
            for i in range(2, maxdivisor+1):
                if number % i == 0:
                    break
                if i == maxdivisor:
                    primes.append(number)
        elif number == 2 or number == 3:
            primes.append(number)

    return sorted(primes)
