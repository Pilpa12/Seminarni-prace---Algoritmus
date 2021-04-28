from math import sqrt


def isprime(number):
    if number > 0:
        divisors = []  # seznam dělitelů
        maxdivisor = round(
            sqrt(number)
        )  # horní hranice čísel, kterými budeme zkoušet dělit zadané číslo
        for i in range(1, maxdivisor + 1):
            if number % i == 0:
                divisors.append(i)

        if len(divisors) > 1:
            print(f"{number} není prvočíslo.")
        else:
            print(f"{number} je prvočíslo.")
    else:
        print("Špatně zadaná hodnota.")


isprime(5)
