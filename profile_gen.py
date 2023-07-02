import random
from itertools import permutations

import numpy as np


def generate_ranking(m):
    return tuple(np.random.permutation(m))


def generate_profile(n, m):
    r = {}
    for _ in range(n):
        add_ranking(r, generate_ranking(m))
    return r


def generate_cartesian_ranking(m_coords_sqrd, d):
    point_sqrd = [random.random() ** 2 for _ in range(d)]
    dists = [np.sqrt(sum([abs(m[i] - point_sqrd[i]) for i in range(d)])) for m in m_coords_sqrd]
    return tuple(np.argsort(dists))

def generate_cartesian_profile(n, m, d):
    m_coords_sqrd = [[random.random() ** 2 for _ in range(d)] for _ in range(m)]
    r = {}
    for _ in range(n):
        add_ranking(r, generate_cartesian_ranking(m_coords_sqrd, d))
    return r

def mallows_dists(m):
    all_rankings = list(permutations(range(m), m))
    dists = {key : -1 for key in all_rankings}
    dists[tuple(range(m))] = 0
    currents = {tuple(range(m))}
    news = set()
    while currents:
        for r in currents:
            for i in range(m - 1):
                r_list = list(r)
                a = r_list[i]
                r_list[i] = r_list[i + 1]
                r_list[i + 1] = a
                r2 = tuple(r_list)
                if dists[r2] == -1:
                    dists[r2] = dists[r] + 1
                    news.add(r2)
        currents = news
        news = set()
    return list(dists.keys()), list(dists.values())

def generate_mallows_profile(n, m, phi, dists):
    r = {}
    rankings = random.choices(dists[0], weights = [phi ** i for i in dists[1]], k = n)
    for i in rankings:
        add_ranking(r, i)
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
