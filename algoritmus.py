from math import sqrt, floor


def getprimes(numbers):
    primes = []  # předpřipravený seznam pro prvočísla
    for number in numbers:
        if number > 3:  # pokud je číslo větší než 3
            maxdivisor = floor(
                sqrt(number)
            )  # horní hranice čísel, kterými budeme zkoušet dělit zadané číslo
            for i in range(2, maxdivisor + 1):
                if number % i == 0:  # pokud je číslo dělitelné beze zbytku
                    break
                if (
                    i == maxdivisor
                ):  # pokud cyklus došel až sem, kontrolované číslo je prvočíslo
                    primes.append(number)
        elif number == 2 or number == 3:  # pokud je číslo rovno 2 nebo 3
            primes.append(number)

    return primes
