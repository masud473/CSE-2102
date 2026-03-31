v=['A','B','C','D','E']
n=len(v)
mat=[ [] for _ in range(n)]
adj=[('A','B'),('B','D'),('D','E'),('E','C'),('C','A'),('A','C')]
for i in adj:
    x=i[0]
    y=i[1]
    mat[v.index(x)].append(y)
for i,l in enumerate(mat):
    print(v[i],end=' -> ')
    for j in l:
        print(j,end=' ')
    print()
