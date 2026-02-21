def gcd(a:int,b:int):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def check(a:int,b:int,c:int):
    return c%gcd(a,b)==0

print(check(12,18,6))
print(check(12,18,5))