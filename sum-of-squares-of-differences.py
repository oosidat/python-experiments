def operations(l1,l2):
    differences = []
    i = 0
    while i < len(l1):
        differences.append((l1[i]-l2[i])**2)
        i = i + 1
    return sum(differences)

lista = [1.0, 2.0, 3.0, 1.0]
listb = [9.0, 5.0, 1.0, 1.0]

print operations(lista,listb)