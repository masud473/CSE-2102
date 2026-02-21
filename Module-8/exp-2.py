def gcd(a:int,b:int):
    if b==0:
        return a
    return gcd(b,a%b)

def inv_modulo(a:int,b:int):
    if b==0:
        return 1,0,a
    else:
        x,y,g=inv_modulo(b,a%b)
        return y,x-a//b*y,g

def solver(a:int,b:int,c:int):
    x=gcd(a,c)     
    if b%x==0:
        q=(inv_modulo(a//x,c//x)[0]%c+c)%c
        ans0= (b//x*q)%c
        return [(ans0+ i*c//x)%c for i in range(x)]
    else:
        return None
def checker(a:int,b:int,c:int):
    x=solver(a,b,c)
    if x:
        for i in x:
            if (a*i-b)%c==0:
                print(f'ans of {a}x = {b} (mod {c}) is {i} and it\'s verified')
    else: 
        print(f'{a}x = {b} (mod {c}) has no solution')
checker(6,3,9)