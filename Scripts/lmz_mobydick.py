# How to use lmz as a module 
# Rememeber the arguments of the spw function: lmz(x,mu)

import lmzoriginal as lmz_t
import pandas as pd

x = pd.read_excel('1M.xlsx', header = None , nrows = 501)
mu = 1
lmztest_result = lmz_t.lmztest(x, mu)
print("lmz test result:", lmztest_result) 