def isfunction(pair:list(tuple[int,int]))->bool:
    domain_set=set()
    for i in pair:
        if len(i)!=2:
            return False
        elif i[0] in domain_set:
            return False
        else:
            domain_set.add(i[0])
    return True
        

print(isfunction([(1,2),(2,5),(4,)]))