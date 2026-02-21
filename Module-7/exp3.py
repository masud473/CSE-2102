def extended_gcd(a:int,b:int):
    if b==0:
        return 1,0,a
    else:
        x,y,g=extended_gcd(b,a%b)
        return y,x-y*(a//b),g

def modular_inv(a:int,b:int):
    x,y,g=extended_gcd(a,b)
    if g==1:
        print(f"Modular inverse of {a} mod {b} is {x if x>0 else x+b}")
    else:
        print(f"Modular inverse of {a} mod {b} does not exist")

modular_inv(11,122)