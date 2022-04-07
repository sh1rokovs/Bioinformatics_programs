import collections

num = int(input())
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


def peptide_cycle_mass(default_peptide):
    temp = sum(default_peptide)
    base_length = len(default_peptide)
    default_peptide = default_peptide + default_peptide[:-1]
    temp1 = [sum(default_peptide[i:i + j]) for j in range(1, base_length) for i in range(base_length)]
    return [0] + sorted(temp1) + [temp]


def peptide_total(default_peptide, default_spectrum):
    def_spectrum = peptide_cycle_mass(default_peptide)
    def_spectrum_counter = collections.Counter(def_spectrum)
    def_spectrum_counter_1 = collections.Counter(default_spectrum)
    return sum((def_spectrum_counter & def_spectrum_counter_1).values())


def leading_total(default_peptide, default_spectrum):
    def_spectrum = peptide_line_mass(default_peptide[1:])
    def_spectrum_counter = collections.Counter(def_spectrum)
    def_spectrum_counter_1 = collections.Counter(default_spectrum)
    return sum((def_spectrum_counter & def_spectrum_counter_1).values())


def app_list(default_peptides):
    return [j + [i] for i in list_r for j in default_peptides]


def peptide_line_mass(default_peptide):
    return [0] + [sum(default_peptide[i:i + j]) for j in range(1, len(default_peptide) + 1)
                  for i in range(len(default_peptide) - j + 1)]


def peptide_order(default_leading, default_spectrum, default_num):
    default_leading.sort(key=lambda x: leading_total(x, default_spectrum), reverse=True)
    if default_num >= len(default_leading):
        return default_leading
    idx = default_num - 1
    min_score = leading_total(default_leading[idx], default_spectrum)
    return [i for i in default_leading if leading_total(i, default_spectrum) >= min_score]


def leading_sequencing_peptide(default_spectrum, default_num):
    leading = [[0]]
    leading_peptide = []
    parent_mass = max(default_spectrum)
    while leading:
        leading = app_list(leading)
        for el in leading[:]:
            if sum(el) == parent_mass:
                if peptide_total(el, default_spectrum) > peptide_total(leading_peptide, default_spectrum):
                    leading_peptide = el[:]
            elif sum(el) > parent_mass:
                leading.remove(el)
        leading = peptide_order(leading, default_spectrum, default_num)
    print("-".join([str(i) for i in leading_peptide[1:]]))
    return leading_peptide


lp = leading_sequencing_peptide(spectrum, num)