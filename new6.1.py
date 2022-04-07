import collections

spectrum = list(map(int, input().split()))
dictionary = {
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
list_react = (' '.join(dictionary.keys())).split(' ')


def reformat_list1(default_list):
    for el in range(len(default_list)):
        default_list[el] = dictionary.setdefault(default_list[el])


reformat_list1(list_react)


def expand(default_peptides):
    return [j + [i] for i in list_react for j in default_peptides]


def peptide_line_mass(default_peptide):
    return [0] + [sum(default_peptide[i:i + l]) for l in range(1, len(default_peptide) + 1)
                  for i in range(len(default_peptide) - l + 1)]


def peptide_cycle_mass(default_peptide):
    temp = sum(default_peptide)
    base_length = len(default_peptide)
    default_peptide = default_peptide + default_peptide[:-1]
    temp1 = [sum(default_peptide[i:i + l]) for l in range(1, base_length) for i in range(base_length)]
    return [0] + sorted(temp1) + [temp]


def consistent(default_peptide, default_spectrum):
    def_peptide_count = collections.Counter(peptide_line_mass(default_peptide[1:]))
    def_spectrum_count = collections.Counter(default_spectrum)
    def_spectrum_count.subtract(def_peptide_count)
    return all([i >= 0 for i in def_spectrum_count.values()])


def sequencing_peptide(default_spectrum):
    peptides_matrix = [[0]]
    parent_mass = max(default_spectrum)
    while peptides_matrix:
        peptides_matrix = expand(peptides_matrix)
        for el in peptides_matrix[:]:
            if sum(el) == parent_mass:
                if peptide_cycle_mass(el[1:]) == default_spectrum:
                    print("-".join([str(i) for i in el[1:]]))
                peptides_matrix.remove(el)
            elif not consistent(el, default_spectrum):
                peptides_matrix.remove(el)


sequencing_peptide(spectrum)
