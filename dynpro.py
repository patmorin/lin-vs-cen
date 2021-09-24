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
            # Found a good pair of colourings, combine them
            # print("Good pair: {}, {}".format(c1, c2))
            s.append(combine_colourings(c1, c2))
            s.append(combine_colourings(c2, c1))
            # print(len(s))
    print()
    return s

def combine_colourings(c1, c2):
    root = [x for x in c1 if sum(x)==1][0]  # todo, inefficient
    return c1.union({combine_pair(root, p) for p in c2})



def pair_has_center(s1, s2):
    for i in range(len(s1)):
        if s1[i]+s2[i] == 1: return True
    return False

def combine_pair(p1, p2):
    return tuple([min(2, p1[i]+p2[i]) for i in range(len(p1))])

if __name__ == "__main__":
    k = int(sys.argv[1])
    colourings = rank_zero_colourings(k)
    rank = 0
    while colourings:
        print("rank {} tree has {} colourings using {} colours".format(rank, len(colourings), k))
        print("Here's one:")
        print(colourings[0])
        # print(colourings)
        colourings = increase_rank(colourings)
        rank += 1
    print("rank {} tree has {} colourings using {} colours".format(rank, len(colourings), k))

    print(colourings)
