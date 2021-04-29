from algoritmus import getprimes
from primes import primeslist
from random import shuffle

numbers = list(range(1, 200))
randomized = numbers
shuffle(randomized)

test_data = {
    "sorted": (numbers, primeslist),
    "reverse sorted": (list(reversed(numbers)), primeslist),
    "randomized": (randomized, primeslist),
}


def test_function(func):
    print(f"Testuji funkci {func.__name__}:")
    for key, value in test_data.items():
        result = func(value[0])
        if result == value[1]:
            print(f"    {key}:'OK'")
        else:
            print(f"    {key}:'ERROR'")


test_function(getprimes)
