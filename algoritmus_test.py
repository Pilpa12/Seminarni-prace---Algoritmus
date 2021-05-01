from algoritmus import getprimes
from random import shuffle
import csv

primeslist = []  # předpřipravený seznam pro prvočísla od 2 do 200

primes_to_200 = open("primes-to-200.csv")  # soubor s prvočísly od 2 do 200
reader = csv.reader(primes_to_200)
for line in reader:  # pro každý řádek v souboru
    for element in line:  # pro každé číslo v řádku
        element = int(element)  # převedeme číslo z typu str na typ int
        primeslist.append(element)  # přidáme číslo do seznamu

numbers = list(range(1, 200))
randomized = numbers
shuffle(randomized)

test_data = {
    "sorted": (numbers),
    "reverse sorted": (list(reversed(numbers))),
    "randomized": (randomized),
}  # data pro testování (seřazený, obracený a zpřeházený seznam čísel od 1 do 200)


def test_function(func):
    test = []  # pomocný seznam
    print(f"Testuji funkci {func.__name__}:")
    for key, value in test_data.items():  # pro každý seznam testovaných čísel
        result = func(value)  # result bude seznam prvočísel vytvořený funkcí getprimes
        for i in result:  # pro každé číslo v seznamu
            if i in primeslist:  # pokud je číslo v seznamu prvočísel od 2 do 200
                test.append(i)  # přidáme číslo do pomocného seznamu test
            else:  # pokud číslo není v seznamu prvočísel od 2 do 200, algoritmus udělal chybu
                print(f"    {key}:'ERROR'")
                break
            if (
                test == result
            ):  # pokud jsou v pomocném seznamu všechna čísla jako v seznamu result, testování je úspěšné
                print(f"    {key}:'OK'")
                test = []


test_function(getprimes)
