import collections

string_peptide = input()
spectrum = list(map(int, input().split()))
# test input information
# 0 99 113 114 128 227 257 299 355 356 370 371 484
# NQEL
dictionary = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186,
}


def peptide_cycle_mass(default_peptide):
    temp = sum(default_peptide)
    base_length = len(default_peptide)
    default_peptide = default_peptide + default_peptide[:-1]
    temp1 = [sum(default_peptide[i:i + l]) for l in range(1, base_length) for i in range(base_length)]
    return [0] + sorted(temp1) + [temp]


def peptide_convert(default_peptide):
    return [dictionary[i] for i in default_peptide]


def peptide_total(default_peptide, default_spectrum):
    def_peptide = peptide_convert(default_peptide)
    def_spectrum = peptide_cycle_mass(def_peptide)
    def_spectrum_counter = collections.Counter(def_spectrum)
    def_spectrum_counter_1 = collections.Counter(default_spectrum)
    return sum((def_spectrum_counter & def_spectrum_counter_1).values())


print(peptide_total(string_peptide, spectrum))

