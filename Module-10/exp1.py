v=['A','B','C','D','E']
n=len(v)
mat=[[0 for _ in range(n)] for x in range(n)]
adj=[('A','B'),('B','D'),('D','E'),('E','C'),('C','A')]
for i in adj:
    x=i[0]
    y=i[1]
    mat[v.index(x)][v.index(y)]=1
for row in mat:
    print(row)
