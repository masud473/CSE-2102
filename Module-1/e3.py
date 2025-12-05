def tautology(statement,variables):
    n=len(variables)
    for i in variables:
        print(i,end=" ")
    print(statement)
    for i in range(1<<n):
        value_list=[]
        for j in range(n):
            x=(i &(1<<(n-1-j)))!=0
            value_list.append(x)
        dictionary =dict(zip(variables,value_list))
        if eval(statement,dictionary)== False:
            return False
    return True
print(tautology("p or not p",'p'))