def gcd(a:int,b:int):
    if a<b:
        return gcd(b,a)
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(10,10))