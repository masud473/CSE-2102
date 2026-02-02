U=[i for i in range(1,10)]
A=[1,4,6]
A=[1 if i in A else 0 for i in U]
print(A)
A=[U[i] for i in range(len(U)) if A[i]]
print(A)