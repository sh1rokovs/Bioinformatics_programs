import collections

dict_one = {"A": 0,
            "C": 1,
            "G": 2,
            "T": 3}
DNA = []
a, b = map(int, input().split())


def prof_kmer(def_dna, a, def_prof):
    best = 0
    ans = def_dna[:a]
    for el in range(len(def_dna) - a + 1):
        answer = 1.0
        for elem, ch in enumerate(def_dna[el:el + a]):
            answer *= def_prof[dict_one[ch]][elem]
        if best < answer:
            best = answer
            ans = def_dna[el:el + a]
    return ans


def def_score(def_motifs):
    score = 0
    cons_k_mer = "".join([collections.Counter([def_motifs[el][elem]
                                               for el in range(len(def_motifs))]).most_common(1)[0][0]
                          for elem in range(len(def_motifs[0]))])
    for el in range(len(def_motifs)):
        for elem in range(len(def_motifs[0])):
            if def_motifs[el][elem] != cons_k_mer[elem]:
                score += 1
    return score


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


def search(def_DNA, k, t):
    res = []
    for el in def_DNA:
        res.append(el[:k])
    for el in range(len(def_DNA[0]) - k - 1):
        def_motifs = [def_DNA[0][el:el + k]]
        for elem in range(1, t):
            prof = [[1 / (2 * (len(def_motifs))) for el in range(len(def_motifs[0]))] for elem in range(4)]
            for element in range(len(def_motifs[0])):
                for iteration in range(len(def_motifs)):
                    prof[dict_one[def_motifs[iteration][element]]][element] += 1 / (2 * (len(def_motifs)))
            pr = prof
            motifs_elem = prof_kmer(def_DNA[elem], k, pr)
            def_motifs.append(motifs_elem)
        if def_score(def_motifs) < def_score(res):
            res = def_motifs[:]
    return res


for el in range(b):
    DNA.insert(el, input())

print("\n".join(search(DNA, a, b)))
iteration_nucle(DNA)
