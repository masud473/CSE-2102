U:set[int]=set([i for i in range(1,10)])
A:set[int]=set([1,4,6])
B:set[int]=set([1,5,7])
print((U-(A|B))==((U-A)&(U-B)))