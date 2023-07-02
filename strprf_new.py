import numpy as np
from itertools import permutations

from sc_functions import *
from extensions import *
from profile_gen import *

def manipulable_count_plurality(p, n_exts):

    count = np.zeros(n_exts, dtype='int8')

    winners, votes, maximum = plurality(p)

    for r in iter(p):
        if r[0] not in winners:
            if len(winners) > 1:
                count[0:3] = 1
                count[4] = 1
                for a in r[1:]:
                    if a in winners:
                        break
                    if votes[a] == maximum - 1:
                        count[3] = 1
                        break
            else:
                for a in r[1:]:
                    if a == winners[0]:
                        break
                    if votes[a] == maximum - 1:
                        count[0:4] = 1
                        break
        else:
            if len(winners) > 2:
                count[4] = 1
    count[5] = count[3] or count[4]

    #TODO: even_chance

    return count


def manipulable_count_borda(p, n_exts):

    count = np.zeros(n_exts, dtype='int8')

    winners, scores, maximum = borda(p)

    for r in iter(p):
        if all(count[:5]):
            break
        p2 = p.copy()
        remove_ranking(p2, r)
        for r2 in permutations(r, len(r)):
            add_ranking(p2, r2)
            w2, _, _ = borda(p2)
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
            remove_ranking(p2, r2)

    count[5] = count[3] or count[4]

    return count

def manipulable_count_inst_runoff(p, n_exts):

    winners, _ = instant_runoff(p)

    for r in iter(p):
        i = r.index(winners[0])
        for j in range(i):
            p2 = p.copy()
            remove_ranking(p2, r)
            r2 = list(r)
            a = r2[0]
            r2[0] = r2[j]
            r2[j] = a
            r2 = tuple(r2)
            add_ranking(p2, r2)
            w2, _ = instant_runoff(p2)
            if w2[0] != winners[0]:
                return np.ones(n_exts, dtype='int8')

    return np.zeros(n_exts, dtype='int8')


def manipulable_count_pareto(p, n_exts):

    # TODO: even_chance

    return np.zeros(n_exts, dtype='int8')


def manipulable_count_omninomi(p, n_exts):

    # TODO: even_chance

    return np.zeros(n_exts, dtype='int8')


def manipulable_count_condorcet(p, n_exts, n):

    # TODO: even_chance

    count = np.zeros(n_exts, dtype='int8')

    winners, tournament = condorcet(p)

    if len(winners) != 1:
        for r in iter(p):
            for i in range(len(tournament)):
                a = r[i]
                for j in range(len(tournament)):
                    b = r[j]
                    if i < j:
                        if tournament[a][b] < (n - 1) / 2:
                            break
                    if i > j:
                        if tournament[a][b] <= (n - 1) / 2:
                            break
                    count[4] = 1
                    count[5] = 1

    return count


def manipulable_count_copeland(p, n_exts):

    count = np.zeros(n_exts, dtype='int8')

    winners, tournament = copeland(p)

    for r in iter(p):
        if all(count[:5]):
            break
        p2 = p.copy()
        remove_ranking(p2, r)
        for r2 in permutations(r, len(r)):
            add_ranking(p2, r2)
            w2, _ = copeland(p2)
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
            remove_ranking(p2, r2)

    count[5] = count[3] or count[4]

    return count


def manipulable_count_top_cycle(p, n_exts):

    count = np.zeros(n_exts, dtype='int8')

    winners, tournament = top_cycle(p)

    for r in iter(p):
        if count[3] and count[4]:
            break
        p2 = p.copy()
        remove_ranking(p2, r)
        for r2 in permutations(r, len(r)):
            add_ranking(p2, r2)
            w2, _ = top_cycle(p2)
            if winners != w2:
                if not count[3]:
                    if optimist(w2, winners, profile_form_change(r)):
                        count[3] = 1
                if not count[4]:
                    if pessimist(w2, winners, profile_form_change(r)):
                        count[4] = 1
            remove_ranking(p2, r2)

    count[5] = count[3] or count[4]

    return count


def manipulable_count_uncovered(p, n_exts):

    count = np.zeros(n_exts, dtype='int8')

    winners, tournament = uncovered_set(p)

    for r in iter(p):
        if all(count[1:5]):
            break
        p2 = p.copy()
        remove_ranking(p2, r)
        for r2 in permutations(r, len(r)):
            add_ranking(p2, r2)
            w2, _ = uncovered_set(p2)
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
            remove_ranking(p2, r2)

    count[5] = count[3] or count[4]

    return count


def manipulable_count_bipartisan():
    pass


def manipulable_count_all(p, n):

    n_scfs = 9
    n_exts = 8

    count = np.zeros((n_scfs, n_exts))

    count[0] = manipulable_count_plurality(p, n_exts)
    count[1] = manipulable_count_borda(p, n_exts)
    count[2] = manipulable_count_inst_runoff(p, n_exts)
    count[3] = manipulable_count_pareto(p, n_exts)
    count[4] = manipulable_count_omninomi(p, n_exts)
    count[5] = manipulable_count_condorcet(p, n_exts, n)
    count[6] = manipulable_count_copeland(p, n_exts)
    count[7] = manipulable_count_top_cycle(p, n_exts)
    count[8] = manipulable_count_uncovered(p, n_exts)
    #count[9] = manipulable_count_bipartisan()

    return count