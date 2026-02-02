U:list[int]=[i for i in range(1,10)]
A:list[int]=[1,4,8]
A:[int]=[1 if i in A else 0 for i in U]# mark elements in the universal set

print(A)
A=[U[i] for i in range(len(U)) if A[i]]
print(A)
