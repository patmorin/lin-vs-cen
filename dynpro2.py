import sys
import itertools
import numpy



def e(k, i):
    return tuple([int(j==i) for j in range(k)])

def rank_zero_colourings(k):
    return [{e(k,i)} for i in range(k)]

def increase_rank(colourings):
    s = []
    i = 0
    for c1, c2 in itertools.combinations(colourings, 2):
        if i % 10000 == 0:
            m = len(colourings)*(len(colourings)-1)//2
            print("{}/{} ({:.1f}%)\r".format(i, m, 100*i/m), end='')
        i += 1
        good_pair = True
        for p1, p2 in itertools.product(c1, c2):
            if not pair_has_center(p1, p2):
                good_pair = False
                break
        if good_pair:
            if not s:
                print("Able to increase rank")
            s.append(combine_colourings(c1, c2))
            s.append(combine_colourings(c2, c1))
    print()
    return eliminate_duplicates(s)


def eliminate_duplicates(colourings):
    if not colourings: return colourings
    a = { str(sorted(colourings[i])) : i for i in range(len(colourings)) }
    return [colourings[a[c]] for c in a]

def combine_colourings(c1, c2):
    root = [x for x in c1 if sum(x)==1][0]  # todo, inefficient
    return c1.union({combine_pair(root, p) for p in c2})

def pair_has_center(s1, s2):
    for i in range(len(s1)):
        if s1[i]+s2[i] == 1: return True
    return False

def combine_pair(p1, p2):
    return tuple([min(2, p1[i]+p2[i]) for i in range(len(p1))])

def filter_pareto_optimal(colourings):
    optimal = list()
    for i1 in range(len(colourings)):
        c1 = colourings[i1]
        keep = True
        # if i % 1000 == 0:
        m = len(colourings)
        discards = i1-len(optimal)
        print("{}/{} ({:.1f}%) [-{}]\r".format(i1, m, 100*i1/m, discards), end='')
        for i2 in itertools.chain(range(i1+1, len(colourings)), optimal):
            c2 = colourings[i2]
            assert(c1 != c2)
            if c2.issubset(c1):
                keep = False
                break
        if keep:
            optimal.append(i1)
    print()
    return [colourings[i] for i in optimal]

    # optimal = list()
    # pareto_optimal = True
    # for i in range(len(colourings)):
    #     c1 = colourings[i]
    #     for j in range(i+1, len(colourings)):
    #         c2 = colourings[j]
    #         if c2.issubset(c1):
    #             pareto_optimal = False
    #             # print("{} eliminates {}".format(c2, c1))
    #             break
    #     if pareto_optimal:
    #         for c2 in optimal:
    #             if c2.issubset(c1):
    #                 pareto_optimal = False
    #                 # print("{} eliminates {}".format(c2, c1))
    #                 break
    #     if pareto_optimal:
    #         optimal.append(c1)
    # return optimal

    # alternate implementation, probably not as fast
    # suboptimal = list
    # for c1, c2 in itertools.combinations(colourings, 2):
    #     if c1.issubset(c2):
    #         suboptimal.add(c2)
    #     elif c2.issubset(c1):
    #         suboptimal.add(c1)
    # return [c for c in colourings if c not in suboptimal]

if __name__ == "__main__":
    k = int(sys.argv[1])
    colourings = rank_zero_colourings(k)
    rank = 0
    while colourings:
        print("rank {} tree has {} colourings using {} colours".format(rank, len(colourings), k))
        # print("Here's one:")
        # print(colourings[0])
        # print("Eliminating non-Pareto-optimal colourings")
        colourings = filter_pareto_optimal(colourings)
        print("rank {} tree has {} Pareto optimal colourings using {} colours".format(rank, len(colourings), k))
        # print(colourings)
        colourings = increase_rank(colourings)
        rank += 1
    print("rank {} tree has {} colourings using {} colours".format(rank, len(colourings), k))

    print(colourings)
