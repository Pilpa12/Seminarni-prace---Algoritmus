from algoritmus import getprimes
from timeit import repeat
import lists  # obsahuje všechny seznamy pro testování

worst_data = {
    "1. ": lists.primes0,
    "2. ": lists.primes1,
    "3. ": lists.primes2,
    "4. ": lists.primes3,
    "5. ": lists.primes4,
    "6. ": lists.primes5,
    "7. ": lists.primes6,
    "8. ": lists.primes7,
    "9. ": lists.primes8,
    "10.": lists.primes9
}  # data pro nejhorší časovou složitost - pouze prvočísla

best_data = {
    "1. ": lists.even0,
    "2. ": lists.even1,
    "3. ": lists.even2,
    "4. ": lists.even3,
    "5. ": lists.even4,
    "6. ": lists.even5,
    "7. ": lists.even6,
    "8. ": lists.even7,
    "9. ": lists.even8,
    "10.": lists.even9
}  # data pro nejlepší časovou složitost - sudá čísla

average_data = {
    "1. ": lists.avg0,
    "2. ": lists.avg1,
    "3. ": lists.avg2,
    "4. ": lists.avg3,
    "5. ": lists.avg4,
    "6. ": lists.avg5,
    "7. ": lists.avg6,
    "8. ": lists.avg7,
    "9. ": lists.avg8,
    "10.": lists.avg9
}  # data pro průměrnou časovou složitost - náhodná čísla

# Všechny seznamy mají stejný počet prvků - 2000


def benchmark_function(function, test_data):
    print(f" Benchmarking function {function.__name__}\n", "-"*31)
    for key, value in test_data.items():
        command = f"{function.__name__}({value})"
        time = min(repeat(command, number=1, repeat=10, globals=globals()))
        print(f" - {key}: {time:.7f} s", end="\n")
    print()


benchmark_function(getprimes, best_data)
benchmark_function(getprimes, worst_data)
benchmark_function(getprimes, average_data)
