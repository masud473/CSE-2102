graph={
    'A':['B','C'],
    'B':['D'],
    'C':['D'],
    'D':['E'],
    'E':[]
}
queue=[]
lst=[]
table={'A':0,
       'B':0,
       'C':0,
       'D':0,
       'E':0}
def traverse(val,lst):
    queue.append(val)
    while queue:
        val=queue.pop()
        lst.append(val)
        for node in graph[val]:
            if not table[node]:
                table[node]=True
                queue.append(node)

for key in graph.keys():
    if not table[key]:
        table[key]=True
        traverse(key,lst)

print(lst)
