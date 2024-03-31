# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:36:45 2024

@author: farismismar
"""

from scipy import optimize
import scipy.special as sc
import numpy as np


# Generalized for non-integer trunks
def erlang_blocking(offered: float, trunks: float) -> float:
    # Implements https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6770771
    if offered == 0:
        return np.nan # if no blocking led to 0 load, then something is wrong.
    
    # inv_b = offered ** (-trunks) * np.exp(offered) * \
    #     sc.gamma(trunks + 1) * sc.gammaincc(trunks + 1, offered)
    
    # return 1. / inv_b
    
    # Applying ln() helps with very large numbers.
    ln_inv_b = -trunks * np.log(offered) + offered + \
        sc.gammaln(trunks + 1) + \
            np.log(sc.gammaincc(trunks + 1, offered))
    
    return np.exp(-ln_inv_b)


def erlang_blocking_vector(x) -> float:
    offered, trunks, gos = x
    p_b = erlang_blocking(offered, trunks)
    error = (p_b - gos) / gos
    return error ** 2


# Uses a global optimizer over a region
def erlang_load(trunks: float, gos: float) -> float:
    offered_max = trunks / (1. - gos)
    bounds = [(0, offered_max), (trunks, trunks), (gos, gos)]   
    result = optimize.shgo(erlang_blocking_vector, bounds=bounds)
    # print(result)
   
    if (result.success):
        return result.x[0]


def offered_to_carried(offered: float, gos: float) -> float:
    # offered is traffic with no blocking
    carried = 0 * gos + offered * (1 - gos)
    assert (carried <= offered)
    return carried


def carried_to_offered(carried: float, gos: float) -> float:
    offered = carried / (1. - gos)
    assert (carried <= offered)
    return offered


n_trunks = 1000
p_b = 0.05

offered = erlang_load(trunks=n_trunks, gos=p_b)
print(offered)
