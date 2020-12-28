def hailstone(n):
    if n == 1:
        return 1
    elif n % 2==0:
        print(n)
        return hailstone(n//2)
    elif n%2==1:
        print(n)
        return hailstone((3*n)+1)
print(hailstone(5))