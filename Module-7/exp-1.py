def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def lcm(a,b):
    return a*b//gcd(a,b)
def info(a,b):
    print(f'GCD of {a},{b} is {gcd(a,b)} and lcm is {lcm(a,b)}')
info(36,60)