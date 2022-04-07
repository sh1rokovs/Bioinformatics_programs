import collections

AminoAcidMasses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]


def expand(peptides):
    return [j + [i] for i in AminoAcidMasses for j in peptides]


def linearMasses(peptide):
    return [0] + [sum(peptide[i:i + l]) for l in range(1, len(peptide) + 1) for i in range(len(peptide) - l + 1)]


def cycloMasses(peptide):
    t = sum(peptide)
    baselen = len(peptide)
    peptide = peptide + peptide[:-1]
    temp = [sum(peptide[i:i + l]) for l in range(1, baselen) for i in range(baselen)]
    return [0] + sorted(temp) + [t]


def consistent(peptide, spectrum):
    peptide_count = collections.Counter(linearMasses(peptide[1:]))
    spectrum_count = collections.Counter(spectrum)
    spectrum_count.subtract(peptide_count)
    return all([i >= 0 for i in spectrum_count.values()])


def cyclopeptidesequensing(spectrum):
    peptides = [[0]]
    parent_mass = max(spectrum)
    while peptides:
        peptides = expand(peptides)
        for peptide in peptides[:]:
            if sum(peptide) == parent_mass:
                if cycloMasses(peptide[1:]) == spectrum:
                    print("-".join([str(i) for i in peptide[1:]]))
                peptides.remove(peptide)
            elif not consistent(peptide, spectrum):
                peptides.remove(peptide)


input_spectrum = list(map(int, input().split()))
cyclopeptidesequensing(input_spectrum)
"""0 97 97 99 101 103 196 198 198 200 202 295 297 299 299 301 394 396 398 400 400 497"""