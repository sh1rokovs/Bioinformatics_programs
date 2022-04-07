from itertools import product
import sys

nucle = ['A', 'C', 'T', 'G']
DNA = []
num = int(input())


def decorator(func):
    return func


@decorator
def compare_dna(def_kmer, def_dna):
    k = len(def_kmer)
    min_k = k + 1
    ctr = 0
    while k == len(def_dna[ctr:ctr + k]):
        itr = 0
        for elem in range(min(len(def_kmer), len(def_dna[ctr:ctr + k]))):
            if def_kmer[elem] != (def_dna[ctr:ctr + k])[elem]:
                itr += 1
        if itr < min_k:
            min_k = itr
        ctr += 1
    return min_k


def iteration_nucle(def_nucle):
    if 'A' in def_nucle[:1]:
        if 'A' in def_nucle[1:2]:
            if 'A' in def_nucle[2:3]:
                if 'A' in def_nucle[3:4]:
                    return def_nucle
        if 'C' in def_nucle[1:2]:
            if 'A' in def_nucle[2:3]:
                if 'A' in def_nucle[3:4]:
                    pass
        if 'T' in def_nucle[1:2]:
            if 'A' in def_nucle[2:3]:
                if 'A' in def_nucle[3:4]:
                    pass
        if 'G' in def_nucle[1:2]:
            if 'A' in def_nucle[2:3]:
                if 'A' in def_nucle[3:4]:
                    pass
    if 'C' in def_nucle[:1]:
        if 'A' in def_nucle[1:2]:
            if 'A' in def_nucle[2:3]:
                if 'A' in def_nucle[3:4]:
                    pass
    if 'T' in def_nucle[:1]:
        if 'A' in def_nucle[1:2]:
            if 'A' in def_nucle[2:3]:
                if 'A' in def_nucle[3:4]:
                    pass
    if 'G' in def_nucle[:1]:
        if 'A' in def_nucle[1:2]:
            if 'A' in def_nucle[2:3]:
                if 'A' in def_nucle[3:4]:
                    pass


def calculation_dna(def_dna, a):
    ans = ""
    dist = sys.maxsize
    for el in product(nucle, repeat=a):
        count = 0
        for elem in def_dna:
            count += compare_dna(el, elem)
        curr_dist = count
        if dist > curr_dist:
            dist = curr_dist
            ans = el
    return "".join(ans)


for el in range(10):
    DNA.insert(el, input())
print(calculation_dna(DNA, num))
