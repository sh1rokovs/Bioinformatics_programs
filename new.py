str = input()
str1 = input()
count = 0

for el in range(len(str1)):
    if str1[el] == str[0]:
        if str1[el:el+len(str)] in str:
            if len(str1[el:el+len(str)]) == len(str):
                count += 1

print(count)
