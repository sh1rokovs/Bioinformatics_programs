import collections

num = int(input())
spectrum = list(map(int, input().split()))
# 9
# 0 71 101 103 113 114 128 131 156 156 172 199 232 242 259 269 270 287 300 303 313 372 372 373 388
# 398 400 414 431 459 469 486 501 501 503 528 545 570 572 572 587 604 614 642 659 673 675 685 700
# 701 701 760 770 773 786 803 804 814 831 841 857 874 901 917 917 942 945 959 960 970 972 1002 1073
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
    return [j + [i] for i in list_react for j in default_peptides]


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
