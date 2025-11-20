def table(str,var):
    var=list(var)
    for i in var:
        print(i, end=" ")
    print(str)
    d={}
    for i in range(1<<len(var)):
        l=[]
        for j in range(len(var)):
            x=(i & (1<<(len(var)-j-1)))!=0
            print('T' if x else 'F',end=' ')
            l.append(x)
        d=dict(zip(var,l))

        print('T' if eval(str,None,d) else 'F')
        
table("p or q",'pq')
table("not(not p and not q)",'pq')

def match(str1,str2,var):
    var=list(var)
    d={}
    for i in range(1<<len(var)):
        l=[]
        for j in range(len(var)):
            x=(i & (1<<(len(var)-j-1)))!=0
            l.append(x)
        d=dict(zip(var,l))
    if eval(str1,None,d)!=eval(str2,None,d):
        print("Not Equivalent")
        return
    print("Equivalent")

match("p or q","not(not p and not q)",'pq')