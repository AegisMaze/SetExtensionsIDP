from itertools import permutations
from profile_gen import *


def kelly(s1, s2, p):
    if s1 == s2:
        return False
    for i in s1:
        for j in s2:
            if p[i] > p[j]:
                return False
    return True

def manipulable(r, scf, ext):
    for p in iter(r.keys()):
        if manipulable_p(r, p, scf, ext):
            return True
    return False

def manipulable_p(r, p, scf, ext):
    w = scf(r)
    remove_ranking(r, p)
    p3 = profile_form_change(p)
    for p2 in permutations(p, len(p)):
        add_ranking(r, p2)
        if ext(scf(r), w, p3):
            return True
        remove_ranking(r, p2)
    add_ranking(r, p)
    return False
