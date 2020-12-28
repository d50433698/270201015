def multip(n,t=3):
    if t == 0:
        return 0
    else:
        return n + multip(n,t-1)
print(multip(4))