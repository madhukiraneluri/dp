def sos(n):
    if n<=2:
        return n
    return sos(n-1)+sos(n-2)
print(sos(5))
