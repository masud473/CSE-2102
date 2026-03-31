v=['A','B','C','D','E']
n=len(v)
mat=[ [] for _ in range(n)]
adj=[('A','B',5),('B','D',3),('D','E',2),('E','C',1),('C','A',4),('A','C',6)]
for i in adj:
    x=i[0]
    y=i[1]
    w=i[2]
    mat[v.index(x)].append((y,w))
for i,l in enumerate(mat):
    print(v[i],end=' -> ')
    for j in l:
        print(j,end=' ')
    print()
