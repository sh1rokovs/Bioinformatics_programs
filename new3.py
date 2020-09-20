str1 = input()
str1 = (' '.join(str1)).split(' ')

for el in range(len(str1)):
    if str1[el] == 'A':
        str1.pop(el)
        str1.insert(el, 'T')
    elif str1[el] == 'C':
        str1.pop(el)
        str1.insert(el, 'G')
    elif str1[el] == 'G':
        str1.pop(el)
        str1.insert(el, 'C')
    elif str1[el] == 'T':
        str1.pop(el)
        str1.insert(el, 'A')

print(''.join(str1)[::-1])
