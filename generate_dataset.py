#%%

from multiprocessing import Pool
import psutil
from helper import *


#%%

print("CPU Count:", psutil.cpu_count())


#%%

if __name__ == '__main__':
    pool = Pool(psutil.cpu_count())
    path  = "/collatz/dbs/"
    create_all(pool,path)
