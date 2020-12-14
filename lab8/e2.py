def isprime(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
            break
    return True

def primes_between(n1,n2):
    liste = []
    for i in range(n1,n2+1):
        if (isprime(i)):
            liste.append(i)
    return liste
print(primes_between(1,20))