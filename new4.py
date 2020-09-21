rna = input()
list1 = []
list3 = []
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

for el in range(len(rna)):
    if len(rna[el*3:(el*3)+3]):
        list1.append(rna[el*3:(el*3)+3])

list2 = ' '.join(dist.keys()).split(' ')
for el in list1:
    for elem in list2:
        for element in dist.setdefault(elem):
            if element == el:
                if el in dist.setdefault('STOP'):
                    break
                else:
                    list3.append(elem)

print(''.join(list3))
