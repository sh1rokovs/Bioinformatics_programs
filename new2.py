s1 = input()
num = int(input())
list1 = []
index = []
max_num = 0
list2 = []

for el in range(len(s1)):
    if s1[el:el+num] in s1[el+num:]:
        if not s1[el:el+num] in list1:
            list1.append(s1[el:el+num])

for el in range(len(list1)):
    index.append(s1.count(list1[el]))

max_num = max(index)
if index.count(max_num) > 1:
    for el in range(len(list1)):
        if index.count(max_num) != 0:
            list2.append(list1[index.index(max_num)])
            index.insert(index.index(max_num), 0)
            index.remove(max_num)
else:
    print(list1[index.index(max_num)])
print(' '.join(list2))
