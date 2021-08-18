import sympy
from sympy.ntheory import factorint
import time
import pandas as pd
import os
import numpy as np
from functools import partial


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

SMALLEST_NUMBER = 3 # since we calculate the previous serie the smallest number is actually one smaller (should not go below 2 since the return value of the collatz could be an empty list)

def create_dataset(start, stop):
    dataset = []
    for num in range(start,stop+1):
        cz_series = collatz_serie(num)
        dataset.append(all_fancy_calculations(cz_series))
    return pd.DataFrame(dataset)


def save_df(df, PATH):

  os.makedirs(PATH,exist_ok=True)
  FILENAME = 'collatz_db_' + time.strftime("%Y%m%d-%H%M%S_") + str(np.random.randint(1e3,1e9)) + '.parquet'
  file = os.path.join(PATH,FILENAME)
  df.to_parquet(file)
  print("Saved to", file)


def create_dataframe(working_range, path):
    start_time = time.time()
    print('## Going from ', working_range[0], "to", working_range[1], "##")
    df = create_dataset(working_range[0], working_range[1])
    df.columns = xheader
    save_df(df, path)
    print("Iteration took", time.time() - start_time)

def create_all(pool,path):

    dist = int(1e7)
    max_num = int(1e10)
    start = 3

    working_range = [[i,i+dist] for i in range(start,max_num,dist)]
    funct = partial(create_dataframe, path=path)
    results = pool.map(funct, working_range)


    return # just returns last df