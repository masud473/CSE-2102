def mod_check(a,b,m):
    return (a+b)%m==((a%m)+(b%m))%m

print(mod_check(17,5,12))