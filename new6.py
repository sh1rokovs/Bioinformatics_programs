list_dna = input()
list_dna = list_dna.split()

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


def reformat_list2(default_list):
    for el in range(len(default_list)):
        default_list[el] = int(default_list[el])


reformat_list1(list_react)
reformat_list2(list_dna)
print(list_dna)
print(type(list_dna[0]))
print(list_react)
print(type(list_react[0]))
print(dictionary.setdefault(137))


def reformat_list(default_list, default_list1):
    for el in default_list:
        for elem in default_list1:
            if el == elem:
                return 10


number = reformat_list(list_dna, list_react)
print(number)


def dna_split(default_list, default_list1):
    list_example = []
    for el in default_list:
        for elem in default_list1:
            if el == elem:
                list_example.append(el)
    return list_example


list_four = dna_split(list_dna, list_react)
print(list_four)
