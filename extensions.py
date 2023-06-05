# returns true if s1 >^K s2 based on p
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


def gardenfoers(s1, s2, p):
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


def opt_pes(s1, s2, p):
    if optimist(s1, s2, p):
        return True
    return pessimist(s1, s2, p)


def singleton(s1, s2, p):
    if len(s1) != 1 or len(s2) != 1:
        return False
    if p[s1[0]] < p[s2[0]]:
        return True
    return False


def even_chance(s1, s2, p):
    v1 = sum([len(p) - p[a] for a in s1]) / float(len(s1))
    v2 = sum([len(p) - p[a] for a in s2]) / float(len(s2))
    return v1 > v2
