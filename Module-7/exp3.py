def extended_gcd(a,b):
    if b==0:
        return 1,0,a
    else:
        x,y,g=extended_gcd(b,a%b)
        return y,x-y*(a//b),g

def modular_inv(a,b):
    x,y,g=extended_gcd(a,b)
    if g==1:
        print(f"Modular inverse of {a} mod {b} is {x if x>0 else x+b}")
    else:
        print(f"Modular inverse of {a} mod {b} does not exist")

modular_inv(7,26)