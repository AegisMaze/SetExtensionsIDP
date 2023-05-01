import numpy as np

def generate_ranking(m):
    return tuple(np.random.permutation(m))

def generate_profile(n,m):
    r = {}
    for _ in range(n):
        add_ranking(r, generate_ranking(m))
    return r

def add_ranking(r, p):
    r[p] = 1 + r[p] if p in r else 1

def remove_ranking(r, p):
    r[p] -= 1
    if r[p] == 0:
        r.pop(p)

def profile_form_change(p):
    p2 = np.zeros(len(p))
    for i in range(len(p)):
        p2[p[i]] = i
    return p2