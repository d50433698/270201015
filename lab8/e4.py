def bintodec(binary):
    binary = binary[::-1]
    sum = 0
    for i in range(len(binary)):
        if int(binary[i]) == 1:
            sum += 2**i
    return sum
print(bintodec("10010"))