import collections

spectrum = list(map(int, input().split()))
our_dict = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186,
}
list_r = [our_dict.get(el) for el in our_dict.keys()]


def peptide_mass(peptide):
    sum_peptide = sum(peptide)
    length = len(peptide)
    sum_peptide_one = [sum((peptide + peptide[:-1])[i:i + j])
                       for j in range(1, length) for i in range(length)]
    return [0] + sorted(sum_peptide_one) + [sum_peptide]


def consist(peptide, def_spectrum):
    reverse(peptide)
    o_reverse(peptide)
    count = collections.Counter([0] + [sum(peptide[1:][i:i + j])
                                       for j in range(1, len(peptide[1:]) + 1)
                                       for i in range(len(peptide[1:]) - j + 1)])
    spec_count = collections.Counter(def_spectrum)
    spec_count.subtract(count)
    return all([i >= 0 for i in spec_count.values()])


def reverse(point):
    for el in range(4):
        point.append(120)
    point.reverse()


def o_reverse(point):
    point.reverse()
    for el in range(4):
        point.pop()


peptides = [[0]]
mas = max(spectrum)
while peptides:
    peptides = [j + [i] for i in list_r for j in peptides]
    for el in peptides[:]:
        reverse(spectrum)
        o_reverse(spectrum)
        if sum(el) == mas:
            if peptide_mass(el[1:]) == spectrum:
                print("-".join([str(i) for i in el[1:]]))
            peptides.remove(el)
        elif not consist(el, spectrum):
            peptides.remove(el)
        reverse(spectrum)
        o_reverse(spectrum)
