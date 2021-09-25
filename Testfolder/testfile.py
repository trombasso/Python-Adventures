lst = [1, 2, 3, 4, 5, 6]

for i in range(1, 6):
    lst[i] = lst[i - 1]

print(lst)

lst2 = [2 * x for x in range(20)]
print(lst2)
print(lst2 * 2)
