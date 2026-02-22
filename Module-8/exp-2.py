def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def inverse_modulo(a,b):
    if b==0:
        return 1,0,a
    else:
        x,y,g=inverse_modulo(b,a%b)
        return y,x-a//b*y,g

def solver(a,b,c):
    x=gcd(a,c)     
    if b%x==0:
        q=(inverse_modulo(a//x,c//x)[0]%c+c)%c
        ans0= (b//x*q)%c
        return [(ans0+ i*c//x)%c for i in range(x)]
    else:
        return None
def solution(a,b,c):
    x=solver(a,b,c)
    if x:
        for i in x:
            print(f'ans of {a}x = {b} (mod {c}) is {i} ')
    else: 
        print(f'{a}x = {b} (mod {c}) has no solution')
solution(14,30,100)