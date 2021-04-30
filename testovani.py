from algoritmus import getprimes
from random import shuffle
import csv

primeslist = []

primes_to_200 = open("primes.csv")
reader = csv.reader(primes_to_200)
for line in reader:
    for element in line:
        element = int(element)
        primeslist.append(element)

numbers = list(range(1, 200))
randomized = numbers
shuffle(randomized)

test_data = {
    "sorted": (numbers),
    "reverse sorted": (list(reversed(numbers))),
    "randomized": (randomized),
}


def test_function(func):
    print(f"Testuji funkci {func.__name__}:")
    for key, value in test_data.items():
        result = func(value)
        if result == primeslist:
            print(f"    {key}:'OK'")
        else:
            print(f"    {key}:'ERROR'")


test_function(getprimes)
