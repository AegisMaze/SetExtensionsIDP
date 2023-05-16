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

def manipulable_count(x, n, m, scf, ext):
    return sum(manipulable(generate_profile(n, m), scf, ext) for _ in range(x))