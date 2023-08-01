from sc_functions import *

def number_to_tournament(n, m):
    t = np.zeros((m, m))
    for i in range(m):
        for j in range(i):
            if n % 2:
                t[i][j] = 1
            else:
                t[i][j] = -1
            t[j][i] = -t[i][j]
            n >>= 1
        t[i][i] = 1
    return t

def profile_to_number(r):
    t = to_tournament(r)
    m = len(t)
    n = 0
    k = 1
    for i in range(m):
        for j in range(i):
            if t[i][j] > t[j][i]:
                n += k
            k <<= 1
    return n