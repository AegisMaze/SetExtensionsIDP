from itertools import permutations
from profile_gen import *

# returns true if s1 >=^K s2 based on p
# s1, s2: sets of alternatives represented as lists of numbers
# p: relation between alternatives represented as list with alternative -> ranking
def kelly(s1, s2, p):
    if s1 == s2:
        return False
    for i in s1:
        for j in s2:
            if p[i] > p[j]:
                return False
    return True

def fishburn(s1, s2, p):
    if s1 == s2:
        return False
    s12 = list(set(s1) - set(s2))
    s21 = list(set(s2) - set(s1))
    for i in s12:
        for j in s2:
            if p[i] > p[j]:
                return False
    for i in s1:
        for j in s21:
            if p[i] > p[j]:
                return False
    return True

def gardenförs(s1, s2, p):
    if s1 == s2:
        return False
    s12 = list(set(s1) - set(s2))
    s21 = list(set(s2) - set(s1))
    if not s12:
        for i in s1:
            for j in s21:
                if p[i] > p[j]:
                    return False
    if not s21:
        for i in s12:
            for j in s2:
                if p[i] > p[j]:
                    return False
    for i in s12:
        for j in s21:
            if p[i] > p[j]:
                return False
    return True

def optimist(s1, s2, p):
    b1 = s1[0]
    for i in s1:
        if p[i] < p[b1]:
            b1 = i
    b2 = s2[0]
    for i in s2:
        if p[i] < p[b2]:
            b2 = i
    return p[b1] < p[b2]

def pessimist(s1, s2, p):
    w1 = s1[0]
    for i in s1:
        if p[i] > p[w1]:
            w1 = i
    w2 = s2[0]
    for i in s2:
        if p[i] > p[w2]:
            w2 = i
    return p[w1] < p[w2]

def singleton(s1, s2, p):
    if len(s1) != 1 or len(s2) != 1:
        return False
    if p[s1[0]] < p[s2[0]]:
        return True
    return False

def manipulable(r, scf, ext):
    w = scf(r)
    for p in iter(r.keys()):
        r2 = r.copy()
        if manipulable_p(r2, p, w, scf, ext):
            return True
    return False

def manipulable_p(r, p, w, scf, ext):
    remove_ranking(r, p)
    p3 = profile_form_change(p)
    for p2 in permutations(p, len(p)):
        add_ranking(r, p2)
        if ext(scf(r), w, p3):
            return True
        remove_ranking(r, p2)
    add_ranking(r, p)
    return False

def manipulable_count(profiles, scf, ext):
    return sum(manipulable(p, scf, ext) for p in profiles)

def manipulable_count_cartesian(profiles, scf, ext):
    return sum(manipulable(p, scf, ext) for p in profiles)