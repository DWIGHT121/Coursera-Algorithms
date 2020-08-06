

a = input("Enter a string")
length = len(a)
list = [a[i:j] for i in range(0, length) for j in range(i+1, length+1)]
print(list)
length2 = len(list)


count = []
for k in range(0, length2):
    count.append(0)


for i in range(0, length2-1):
    for j in range(i+1, length2):
        if list[i] == list[j]:
            count[i] += 1


for i in range(0, length2-1):
    if count[i] > count[i+1]:
        var = count[i]
        winner = list[i]
    if count[i+1] > count[i]:
        var = count[i+1]
        winner = list[i+1]


print(winner)
print(var+1)
