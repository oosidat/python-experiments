def operation(list1,list2):
    differences = []    
    for i, item in enumerate(list1):
        differences.append((item - list2[i])**2)
    return sum(differences)

lista = [1.0, 2.0, 3.0]
listb = [9.0, 5.0, 1.0]

print operation(lista,listb)

def operation2(list1, list2):
    return sum([(i - j)**2 for i,j in zip(list1, list2)])

print operation2(lista, listb)