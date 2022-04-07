from itertools import product

nucle = ['A', 'C', 'T', 'G']
DNA = []


def compare_dna(def_kmer, def_DNA, b):
    for el in def_DNA:
        kmer_string = False
        ctr = 0
        while len(def_kmer) == len(el[ctr:ctr + len(def_kmer)]):
            s = el[ctr:ctr + len(def_kmer)]
            ir = 0
            for elem in range(min(len(def_kmer), len(s))):
                if def_kmer[elem] != s[elem]:
                    ir += 1
            if ir <= b:
                kmer_string = True
            ctr += 1
        if not kmer_string:
            return False
    return True


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


x, y = map(int, input().split())
for el in range(4):
    DNA.insert(el, input())
motif = set()
for el in product(nucle, repeat=x):
    if compare_dna(el, DNA, y):
        motif.add("".join(el))
print(" ".join(sorted(motif)))
iteration_nucle(nucle)
