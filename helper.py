import sympy
from sympy.ntheory import factorint


def collatz_serie(n: int) -> int:
    ret = [n]
    while (n > 1):
        if n % 2 == 0:
            _n = int(n / 2)
        else:
            _n = n * 3 + 1
        n = _n
        ret.append(n)
    return ret



xheader = ["Number",
           "Length",
           "Max",
           "IsEven",
           "nPrimes",
           "Smallest_Prime",
           "nSmallest_Prim",
           "Biggest_Prime",
           "nBiggest_Prime",
           "isPrime"]


def all_fancy_calculations(serie):
    calculations = list()
    num_in_question = serie[0]
    fac_n = factorint(num_in_question)

    calculations.append(num_in_question)  # Starting number
    calculations.append(len(serie))  # Length of series
    calculations.append(max(serie))  # Max of number series
    calculations.append(num_in_question % 2 == 0)  # Is even?
    calculations.append(len(fac_n))  # how long fac(n)
    calculations.append(min(fac_n))  # smallest prime when fac n
    calculations.append(fac_n[min(fac_n)])  # how often does the smallest prime appear when fac n
    calculations.append(max(fac_n))  # biggest prime when fac n
    calculations.append(fac_n[max(fac_n)])  # how often does the biggest prime appear when fac n
    calculations.append(sympy.isprime(num_in_question))  # is prime?

    return calculations
