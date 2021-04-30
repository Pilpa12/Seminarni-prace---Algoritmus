from algoritmus import getprimes
from timeit import repeat
import lists

best_data = {
    "1.": lists.primes1even,
    "2.": lists.primes2even,
    "3.": lists.primes3even,
    "4.": lists.primes4even,
    "5.": lists.primes5even,
    "6.": lists.primes6even,
    "7.": lists.primes7even,
    "8.": lists.primes8even,
    "9.": lists.primes9even
}

worst_data = {
    "1.": lists.primes1,
    "2.": lists.primes2,
    "3.": lists.primes3,
    "4.": lists.primes4,
    "5.": lists.primes5,
    "6.": lists.primes6,
    "7.": lists.primes7,
    "8.": lists.primes8,
    "9.": lists.primes9
}

average_data = {
    "1.": lists.nums1,
    "2.": lists.nums2,
    "3.": lists.nums3,
    "4.": lists.nums4,
    "5.": lists.nums5,
    "6.": lists.nums6,
    "7.": lists.nums7,
    "8.": lists.nums8,
    "9.": lists.nums9
}


def benchmark_function(function, test_data):
    print(f" Benchmarking function {function.__name__}\n", "-"*31)
    for key, value in test_data.items():
        command = f"{function.__name__}({value})"
        time = min(repeat(command, number=1, repeat=1, globals=globals()))
        print(f" - {key}: {time:.7f} s", end="\n")
    print()


benchmark_function(getprimes, best_data)
benchmark_function(getprimes, worst_data)
benchmark_function(getprimes, average_data)
