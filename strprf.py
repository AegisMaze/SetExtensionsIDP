from itertools import permutations
from profile_gen import *


def manipulable(r, scf, ext):
    w = scf(r)[0]
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
        if ext(scf(r)[0], w, p3):
            #print(p, p2, w, scf(r)[0])
            return True
        remove_ranking(r, p2)
    add_ranking(r, p)
    return False


def manipulable_count(profiles, scf, ext):
    return [manipulable(p, scf, ext) for p in profiles]


def manipulable_count_cartesian(profiles, scf, ext):
    return sum(manipulable(p, scf, ext) for p in profiles)