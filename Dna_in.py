dna = input()
code = input()
dist = {
    'A': ['GCA', 'GCU', 'GCC', 'GCG'],
    'C': ['UGC', 'UGU'],
    'D': ['GAU', 'GAC'],
    'E': ['GAA', 'GAG'],
    'G': ['GGA', 'GGG', 'GGC', 'GGU'],
    'F': ['UUC', 'UUU'],
    'H': ['CAU', 'CAC'],
    'I': ['AUU', 'AUC', 'AUA'],
    'K': ['AAA', 'AAG'],
    'L': ['UUG', 'UUA', 'CUU', 'CUC', 'CUA', 'CUG'],
    'M': ['AUG'],
    'N': ['AAC', 'AAU'],
    'P': ['CCA', 'CCU', 'CCG', 'CCC'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'S': ['AGC', 'AGU', 'UCG', 'UCA', 'UCC', 'UCU'],
    'T': ['ACG', 'ACA', 'ACC', 'ACU'],
    'Y': ['UAC', 'UAU'],
    'V': ['GUG', 'GUA', 'GUC', 'GUU'],
    'W': ['UGG'],
    'Q': ['CAA', 'CAG'],
    'STOP': ['UGA', 'UAG', 'UAA']
}


def multiply_list(a, b):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            c.append(a[i] + b[j])
    return c


def dna_in_dna1(dna):
    dna1 = []
    for el in dna:
        if el == 'A':
            dna1.append('T')
        elif el == 'T':
            dna1.append('A')
        elif el == 'G':
            dna1.append('C')
        elif el == 'C':
            dna1.append('G')
    return ''.join(dna1)


def dna_in_rna(dna):
    rna = []
    if 'T' in dna:
        for el in dna:
            if el == 'A':
                rna.append('U')
            elif el == 'T':
                rna.append('A')
            elif el == 'G':
                rna.append('C')
            elif el == 'C':
                rna.append('G')
        return ''.join(rna)
    elif 'U' in dna:
        for el in dna:
            if el == 'U':
                rna.append('A')
            elif el == 'A':
                rna.append('T')
            elif el == 'C':
                rna.append('G')
            elif el == 'G':
                rna.append('C')
        return ''.join(rna)


list1 = []
for el in code:
    list1.append(dist.setdefault(el))

r = 0
for el in range(len(list1) - 1):
    if el == 0:
        r = list1[el]
    r = multiply_list(r, list1[el + 1])

list3 = []
for el in r:
    list3.append(dna_in_dna1(dna_in_rna(el)))
for el in r:
    list3.append(dna_in_rna(el[::-1]))

i = len(list3[0])
list4 = []
for el in list3:
    for elem in range(len(dna)):
        if dna[elem:elem+i] == el:
            if not len(dna[elem:elem+i]) < i:
                list4.append(dna[elem:elem+i])

for el in list4:
    print(el)
