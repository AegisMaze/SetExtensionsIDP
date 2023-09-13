import numpy as np
from itertools import permutations

from sc_functions import *
from extensions import *
from profile_gen import *
from tourneys import *

def manipulable_count_plurality(p, n_exts):
    count = np.zeros(n_exts)
    count2 = np.zeros(n_exts)

    winners, k_winners = plurality(p)

    for r in iter(p):
        if count[7] and count2[7]: #all(count[:5]) and count[7] and all(count2[:5]) and count2[7]:
            break
        if not (len(winners) == 1 and winners[0] == r[0]):
            p2 = p.copy()
            remove_ranking(p2, r)
            r2 = list(r).copy()
            for i in range(len(r2) - 1):
                r2[0] = (r2[0] + 1) % len(r)
                add_ranking(p2, tuple(r2))
                w2, kw2 = plurality(p2)
                pfc = profile_form_change(r)
                if winners != w2:
                    """if not count[0]:
                        if kelly(w2, winners, pfc):
                            count[0:3] = 1
                    if not count[3]:
                        if optimist(w2, winners, pfc):
                            count[3] = 1
                    if not count[4]:
                        if pessimist(w2, winners, pfc):
                            count[4] = 1"""
                    if not count[7]:
                        if even_chance(w2, winners, pfc):
                            count[7] = 1
                if k_winners != kw2:
                    """if not count2[0]:
                        if kelly(kw2, k_winners, pfc):
                            count2[0:3] = 1
                    if not count2[3]:
                        if optimist(kw2, k_winners, pfc):
                            count2[3] = 1
                    if not count2[4]:
                        if pessimist(kw2, k_winners, pfc):
                            count2[4] = 1"""
                    if not count2[7]:
                        if even_chance(kw2, k_winners, pfc):
                            count2[7] = 1
                remove_ranking(p2, tuple(r2))
        elif not count2[7]: #(all(count2[:5]) and count2[7]):
            p2 = p.copy()
            remove_ranking(p2, r)
            r2 = list(r).copy()
            for i in range(len(r2) - 1):
                r2[0] = (r2[0] + 1) % len(r)
                add_ranking(p2, tuple(r2))
                _, kw2 = plurality(p2)
                pfc = profile_form_change(r)
                if k_winners != kw2:
                    """if not count2[0]:
                        if kelly(kw2, k_winners, pfc):
                            count2[0:3] = 1
                    if not count2[3]:
                        if optimist(kw2, k_winners, pfc):
                            count2[3] = 1
                    if not count2[4]:
                        if pessimist(kw2, k_winners, pfc):
                            count2[4] = 1"""
                    if not count2[7]:
                        if even_chance(kw2, k_winners, pfc):
                            count2[7] = 1
                remove_ranking(p2, tuple(r2))

    count[5] = count[3] or count[4]
    count2[5] = count2[3] or count2[4]

    return count, count2


def manipulable_count_borda(p, n_exts):

    count = np.zeros(n_exts)
    count2 = np.zeros(n_exts)

    winners, k_winners = borda(p)

    for r in iter(p):
        if all(count[:5]) and all(count[6:]) and all(count2[:5]) and all(count2[6:]):
            break
        if not (len(winners) == 1 and winners[0] == r[0]):
            p2 = p.copy()
            remove_ranking(p2, r)
            for r2 in permutations(r, len(r)):
                add_ranking(p2, r2)
                w2, kw2 = borda(p2)
                if winners != w2:
                    pfc = profile_form_change(r)
                    if not count[0]:
                        if kelly(w2, winners, pfc):
                            count[0] = 1
                    if not count[1]:
                        if fishburn(w2, winners, pfc):
                            count[1] = 1
                    if not count[2]:
                        if gardenfoers(w2, winners, pfc):
                            count[2] = 1
                    if not count[3]:
                        if optimist(w2, winners, pfc):
                            count[3] = 1
                    if not count[4]:
                        if pessimist(w2, winners, pfc):
                            count[4] = 1
                    if not count[6]:
                        if singleton(w2, winners, pfc):
                            count[6] = 1
                    if not count[7]:
                        if even_chance(w2, winners, pfc):
                            count[7] = 1
                if k_winners != kw2:
                    pfc = profile_form_change(r)
                    if not count2[0]:
                        if kelly(kw2, k_winners, pfc):
                            count2[0] = 1
                    if not count2[1]:
                        if fishburn(kw2, k_winners, pfc):
                            count2[1] = 1
                    if not count2[2]:
                        if gardenfoers(kw2, k_winners, pfc):
                            count2[2] = 1
                    if not count2[3]:
                        if optimist(kw2, k_winners, pfc):
                            count2[3] = 1
                    if not count2[4]:
                        if pessimist(kw2, k_winners, pfc):
                            count2[4] = 1
                    if not count2[6]:
                        if singleton(kw2, k_winners, pfc):
                            count2[6] = 1
                    if not count2[7]:
                        if even_chance(kw2, k_winners, pfc):
                            count2[7] = 1
                remove_ranking(p2, r2)
        elif not (all(count2[:5]) and all(count2[6:])):
            p2 = p.copy()
            remove_ranking(p2, r)
            for r2 in permutations(r, len(r)):
                add_ranking(p2, r2)
                _, kw2 = borda(p2)
                if k_winners != kw2:
                    pfc = profile_form_change(r)
                    if not count2[0]:
                        if kelly(kw2, k_winners, pfc):
                            count2[0] = 1
                    if not count2[1]:
                        if fishburn(kw2, k_winners, pfc):
                            count2[1] = 1
                    if not count2[2]:
                        if gardenfoers(kw2, k_winners, pfc):
                            count2[2] = 1
                    if not count2[3]:
                        if optimist(kw2, k_winners, pfc):
                            count2[3] = 1
                    if not count2[4]:
                        if pessimist(kw2, k_winners, pfc):
                            count2[4] = 1
                    if not count2[6]:
                        if singleton(kw2, k_winners, pfc):
                            count2[6] = 1
                    if not count2[7]:
                        if even_chance(kw2, k_winners, pfc):
                            count2[7] = 1
                remove_ranking(p2, r2)

    count[5] = count[3] or count[4]
    count2[5] = count2[3] or count2[4]

    return count, count2

def manipulable_count_inst_runoff(p, n, n_exts):

    count = np.zeros(n_exts)

    winners, _ = instant_runoff(p)

    for r in iter(p):
        if all(count[:5]) and all(count[6:]):
            break
        if not (len(winners) == 1 and winners[0] == r[0]):
            p2 = p.copy()
            remove_ranking(p2, r)
            for r2 in permutations(r, len(r)):
                add_ranking(p2, r2)
                w2, _ = instant_runoff(p2)
                if winners != w2:
                    pfc = profile_form_change(r)
                    if not count[0]:
                        if kelly(w2, winners, pfc):
                            count[0] = 1
                    if not count[1]:
                        if fishburn(w2, winners, pfc):
                            count[1] = 1
                    if not count[2]:
                        if gardenfoers(w2, winners, pfc):
                            count[2] = 1
                    if not count[3]:
                        if optimist(w2, winners, pfc):
                            count[3] = 1
                    if not count[4]:
                        if pessimist(w2, winners, pfc):
                            count[4] = 1
                    if not count[6]:
                        if singleton(w2, winners, pfc):
                            count[6] = 1
                    if not count[7]:
                        if even_chance(w2, winners, pfc):
                            count[7] = 1
                remove_ranking(p2, r2)

    count[5] = count[3] or count[4]

    return count


def manipulable_count_pareto(p, n_exts):

    count = np.zeros(n_exts)

    winners, _ = pareto(p)

    for r in iter(p):
        if all(count[2:5]) and all(count[6:]):
            break
        if not (len(winners) == 1 and winners[0] == r[0]):
            p2 = p.copy()
            remove_ranking(p2, r)
            for r2 in permutations(r, len(r)):
                add_ranking(p2, r2)
                w2, _ = pareto(p2)
                if winners != w2:
                    pfc = profile_form_change(r)
                    if not count[2]:
                        if gardenfoers(w2, winners, pfc):
                            count[2] = 1
                    if not count[3]:
                        if optimist(w2, winners, pfc):
                            count[3] = 1
                    if not count[4]:
                        if pessimist(w2, winners, pfc):
                            count[4] = 1
                    if not count[6]:
                        if singleton(w2, winners, pfc):
                            count[6] = 1
                    if not count[7]:
                        if even_chance(w2, winners, pfc):
                            count[7] = 1
                remove_ranking(p2, r2)

    count[5] = count[3] or count[4]

    return count


def manipulable_count_omninomi(p, n_exts):
    count = np.zeros(n_exts)

    winners, _ = omninomination(p)

    for r in iter(p):
        if not (len(winners) == 1 and winners[0] == r[0]):
            p2 = p.copy()
            remove_ranking(p2, r)
            r2 = list(r).copy()
            for i in range(len(r2) - 1):
                r2[0] = (r2[0] + 1) % len(r)
                add_ranking(p2, tuple(r2))
                w2, _ = omninomination(p2)
                if winners != w2:
                    pfc = profile_form_change(r)
                    if not count[7]:
                        if even_chance(w2, winners, pfc):
                            count[7] = 1
                            return count
                remove_ranking(p2, tuple(r2))

    return count


def manipulable_count_condorcet(p, n_exts, res):
    count = np.zeros(n_exts)

    winners = res[profile_to_number(p)]

    for r in iter(p):
        if all(count[3:5]) and count[7]:
            break
        if not (len(winners) == 1 and winners[0] == r[0]):
            p2 = p.copy()
            remove_ranking(p2, r)
            for r2 in permutations(r, len(r)):
                add_ranking(p2, r2)
                w2 = res[profile_to_number(p2)]
                if winners != w2:
                    pfc = profile_form_change(r)
                    if not count[3]:
                        if optimist(w2, winners, pfc):
                            count[3] = 1
                    if not count[4]:
                        if pessimist(w2, winners, pfc):
                            count[4] = 1
                    if not count[7]:
                        if even_chance(w2, winners, pfc):
                            count[7] = 1
                remove_ranking(p2, r2)

    count[5] = count[3] or count[4]

    return count


def manipulable_count_copeland(p, n_exts, res):

    count = np.zeros(n_exts)

    winners = res[profile_to_number(p)]

    for r in iter(p):
        if all(count[:5]) and all(count[6:]):
            break
        if not (len(winners) == 1 and winners[0] == r[0]):
            p2 = p.copy()
            remove_ranking(p2, r)
            for r2 in permutations(r, len(r)):
                add_ranking(p2, r2)
                w2 = res[profile_to_number(p2)]
                if winners != w2:
                    pfc = profile_form_change(r)
                    if not count[0]:
                        if kelly(w2, winners, pfc):
                            count[0] = 1
                    if not count[1]:
                        if fishburn(w2, winners, pfc):
                            count[1] = 1
                    if not count[2]:
                        if gardenfoers(w2, winners, pfc):
                            count[2] = 1
                    if not count[3]:
                        if optimist(w2, winners, pfc):
                            count[3] = 1
                    if not count[4]:
                        if pessimist(w2, winners, pfc):
                            count[4] = 1
                    if not count[6]:
                        if singleton(w2, winners, pfc):
                            count[6] = 1
                    if not count[7]:
                        if even_chance(w2, winners, pfc):
                            count[7] = 1
                remove_ranking(p2, r2)

    count[5] = count[3] or count[4]

    return count


def manipulable_count_top_cycle(p, n_exts, res):

    count = np.zeros(n_exts)
    count2 = np.zeros(n_exts)

    winners = res[profile_to_number(p)]
    k_winners = winners if len(winners) == 1 else winners[:2]

    for r in iter(p):
        if count[3] and count[4] and count[7] and count2[3] and count2[4] and count2[7]:
            break
        if not (len(winners) == 1 and winners[0] == r[0]):
            p2 = p.copy()
            remove_ranking(p2, r)
            for r2 in permutations(r, len(r)):
                add_ranking(p2, r2)
                w2 = res[profile_to_number(p2)]
                kw2 = w2 if len(w2) == 1 else w2[:2]
                pfc = profile_form_change(r)
                if winners != w2:
                    if not count[3]:
                        if optimist(w2, winners, pfc):
                            count[3] = 1
                    if not count[4]:
                        if pessimist(w2, winners, pfc):
                            count[4] = 1
                    if not count[7]:
                        if even_chance(w2, winners, pfc):
                            count[7] = 1
                if k_winners != kw2:
                    if not count2[3]:
                        if optimist(w2, winners, pfc):
                            count2[3] = 1
                    if not count2[4]:
                        if pessimist(w2, winners, pfc):
                            count2[4] = 1
                    if not count2[7]:
                        if even_chance(w2, winners, pfc):
                            count2[7] = 1
                remove_ranking(p2, r2)
        elif not (count2[3] and count2[4] and count2[7]):
            p2 = p.copy()
            remove_ranking(p2, r)
            for r2 in permutations(r, len(r)):
                add_ranking(p2, r2)
                w2 = res[profile_to_number(p2)]
                kw2 = w2 if len(w2) == 1 else w2[:2]
                if k_winners != kw2:
                    pfc = profile_form_change(r)
                    if not count2[3]:
                        if optimist(w2, winners, pfc):
                            count2[3] = 1
                    if not count2[4]:
                        if pessimist(w2, winners, pfc):
                            count2[4] = 1
                    if not count2[7]:
                        if even_chance(w2, winners, pfc):
                            count2[7] = 1
                remove_ranking(p2, r2)

    count[5] = count[3] or count[4]
    count2[5] = count2[3] or count2[4]

    return count, count2


def manipulable_count_uncovered(p, n_exts, res):

    count = np.zeros(n_exts)

    winners = res[profile_to_number(p)]

    for r in iter(p):
        if all(count[1:5]) and count[7]:
            break
        if not (len(winners) == 1 and winners[0] == r[0]):
            p2 = p.copy()
            remove_ranking(p2, r)
            for r2 in permutations(r, len(r)):
                add_ranking(p2, r2)
                w2 = res[profile_to_number(p2)]
                if winners != w2:
                    pfc = profile_form_change(r)
                    if not count[1]:
                        if fishburn(w2, winners, pfc):
                            count[1] = 1
                    if not count[2]:
                        if gardenfoers(w2, winners, pfc):
                            count[2] = 1
                    if not count[3]:
                        if optimist(w2, winners, pfc):
                            count[3] = 1
                    if not count[4]:
                        if pessimist(w2, winners, pfc):
                            count[4] = 1
                    if not count[7]:
                        if even_chance(w2, winners, pfc):
                            count[7] = 1
                remove_ranking(p2, r2)

    count[5] = count[3] or count[4]

    return count


def manipulable_count_bipartisan(p, n_exts, res):
    count = np.zeros(n_exts)

    winners = res[profile_to_number(p)]

    for r in iter(p):
        if all(count[1:5]) and count[7]:
            break
        if not (len(winners) == 1 and winners[0] == r[0]):
            p2 = p.copy()
            remove_ranking(p2, r)
            for r2 in permutations(r, len(r)):
                add_ranking(p2, r2)
                w2 = res[profile_to_number(p2)]
                if winners != w2:
                    pfc = profile_form_change(r)
                    if not count[1]:
                        if fishburn(w2, winners, pfc):
                            count[1] = 1
                    if not count[2]:
                        if gardenfoers(w2, winners, pfc):
                            count[2] = 1
                    if not count[3]:
                        if optimist(w2, winners, pfc):
                            count[3] = 1
                    if not count[4]:
                        if pessimist(w2, winners, pfc):
                            count[4] = 1
                    if not count[7]:
                        if even_chance(w2, winners, pfc):
                            count[7] = 1
                remove_ranking(p2, r2)

    count[5] = count[3] or count[4]

    return count


def manipulable_count_all(p, n, res):

    n_scfs = 13
    n_exts = 8

    count = np.zeros((n_scfs, n_exts))

    count[0], count[10] = manipulable_count_plurality(p, n_exts)
    count[1], count[11] = manipulable_count_borda(p, n_exts)
    count[2] = manipulable_count_inst_runoff(p, n, n_exts)
    count[3] = manipulable_count_pareto(p, n_exts)
    count[4] = manipulable_count_omninomi(p, n_exts)
    count[5] = manipulable_count_condorcet(p, n_exts, res[0])
    count[6] = manipulable_count_copeland(p, n_exts, res[1])
    count[7], count[12] = manipulable_count_top_cycle(p, n_exts, res[2])
    count[8] = manipulable_count_uncovered(p, n_exts, res[3])
    count[9] = manipulable_count_bipartisan(p, n_exts, res[4])

    return count