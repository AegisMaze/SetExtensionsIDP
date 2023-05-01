import numpy as np


def plurality(r):
    m = len(next(iter(r)))
    count = np.zeros(m)
    for k, v in r.items():
        count[k[0]] += v
    maximum = max(count)
    return sorted([i for i, j in enumerate(count) if j == maximum])


def borda(r):
    m = len(next(iter(r)))
    count = np.zeros(m)
    for k, v in r.items():
        for i in range(m):
            count[k[i]] += v * (m - i - 1)
    maximum = max(count)
    return sorted([i for i, j in enumerate(count) if j == maximum])
