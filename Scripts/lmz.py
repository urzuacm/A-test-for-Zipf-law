import numpy as np
import statistics as st
import scipy.stats as stats
import pandas as pd

def lmztest(x):
    xn = x.values[-1]
    n = len(x)
    z1 = 1 - np.mean(np.log(x / xn ))
    z2 = 0.5 - np.mean(xn / x)
    lmz = 4 * n * (z1 ** 2 + 6 * (z1 * z2) + 12 * (z2 ** 2))
    p_value = 1 - stats.chi2.cdf (lmz, df=2)
    return lmz, p_value

x = pd.read_excel("MET.xlsx", header = None)
print (lmztest(x))
