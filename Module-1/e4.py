def truth_table(statement,variables):
    n=len(variables)
    for i in variables:
        print(i,end=" ")
    print(statement)
    for i in range(1<<n):
        value_list=[]
        for j in range(n):
            x=(i &(1<<(n-1-j)))!=0
            print('T' if x else 'F',end=" ")
            value_list.append(x)
        dictionary =dict(zip(variables,value_list))
        print(end="  ")
        print('T' if eval(statement,dictionary) else 'F')
truth_table("(p or q)<= r", 'pqr')
        