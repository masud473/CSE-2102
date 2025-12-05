def equivalence(statement1,statement2,variables):
    n=len(variables)
    for i in range(1<<n):
        value_list=[]
        for j in range(n):
            x=(i &(1<<(n-1-j)))!=0
            value_list.append(x)
        dictionary =dict(zip(variables,value_list))
        if eval(statement1,dictionary)!=eval(statement2,dictionary):
            return False
    return True
print("Equivalent" if equivalence(" (p or q) and (not p or q) ",'q', 'pq') else "Not Equivalent")
        