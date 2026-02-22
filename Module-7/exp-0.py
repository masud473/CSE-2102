def isdivisible(a,b,c):
    if a%b==0 and a%c==0:
        print(f'{a} is divisible by both {b} and {c}')
    else:
        print(f'{a} is not divisible by both {b} and {c}')

isdivisible(72,4,6)