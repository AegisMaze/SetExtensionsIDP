import queue

import numpy as np
import scipy.optimize as opt


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


def instant_runoff(r):
    profile = list(r.items())
    n = len(profile)
    indices = np.zeros(n, int)
    m = len(profile[0][0])
    removed = np.zeros(m, bool)
    while True:
        count = np.zeros(m)
        for i in range(n):
            a = profile[i]
            count[a[0][indices[i]]] += a[1]
        maximum = -1
        minimum = -1
        for i in range(m):
            if not removed[i]:
                if count[i] > maximum:
                    maximum = count[i]
                if count[i] < minimum or minimum == -1:
                    minimum = count[i]
        if maximum == minimum:
            return [i for i in range(m) if removed[i] != 1]
        for i in range(m):
            if count[i] == minimum:
                removed[i] = True
        for i in range(n):
            while removed[profile[i][0][indices[i]]]:
                indices[i] += 1


def pareto(r):
    m = len(next(iter(r)))
    dom = np.zeros((m, m), bool)
    for k, _ in r.items():
        for i in range(m):
            for j in range(i + 1):
                dom[k[j]][k[i]] = True
    return [i for i in range(m) if all(dom[i])]

def to_tournament(r):
    m = len(next(iter(r)))
    t = np.zeros((m, m), int)
    for k, v in r.items():
        for i in range(m):
            for j in range(i):
                t[k[j]][k[i]] += v
    return t

def to_simple_tournament(r):
    t = to_tournament(r)
    m = len(t)
    st = np.zeros((m, m), int)
    for i in range(m):
        for j in range(i):
            if t[i][j] > t[j][i]:
                st[i][j] = 1
            else:
                if t[i][j] < t[j][i]:
                    st[i][j] = -1
            st[j][i] = -st[i][j]
    return st

def copeland(r):
    t = to_tournament(r)
    m = len(t)
    count = np.zeros(m, int)
    for i in range(m):
        for j in range(i):
            if t[i][j] > t[j][i]:
                count[i] += 2
            else:
                if t[i][j] < t[j][i]:
                    count[j] += 2
                else:
                    count[i] += 1
                    count[j] += 1
        count[i] += 1
    maximum = max(count)
    return [i for i in range(m) if count[i] == maximum]

def top_cycle(r):
    t = to_tournament(r)
    m = len(t)
    dom = np.zeros(m, bool)
    q = queue.Queue()
    for i in copeland(r):
        q.put(i)
        dom[i] = True
    while not q.empty():
        i = q.get()
        for j in range(m):
            if not dom[j] and t[j][i] >= t[i][j]:
                q.put(j)
                dom[j] = True
    return [i for i in range(m) if dom[i]]

def uncovered_set(r):
    t = to_tournament(r)
    m = len(t)
    dom = np.zeros((m, m), bool)
    for i in range(m):
        for j in range(i):
            if t[i][j] > t[j][i]:
                dom[i][j] = True
            if t[i][j] < t[j][i]:
                dom[j][i] = True
    id = np.zeros((m,m), bool)
    np.fill_diagonal(id, True)
    matrix = id | dom | (dom @ dom)
    return [i for i in range(m) if all(matrix[i])]

def bipartisan_set(r):
    t = to_simple_tournament(r)
    m = len(t)
    zeros = np.zeros(m)
    ones = np.ones(m)
    res = opt.linprog(c=zeros, A_ub=t, b_ub=zeros, A_eq=np.ones((m,m)), b_eq=ones, bounds=(0, 1))
    return [i for i in range(m) if res.x[i] > 0]