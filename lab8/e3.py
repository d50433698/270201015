import random
def get_rand_list(n1,n2,N):
    liste = []
    for i in range(N):
        liste.append(random.randint(n1,n2+1))
    return liste
def intersection(l1,l2):
    inter = []
    for lst1 in l1:
        for lst2 in l2:
            if lst1 == lst2:
                inter.append(lst1)
                break
    return inter

lyt = intersection(get_rand_list[1,10,5],get_rand_list[1,10,5])
print(lyt)