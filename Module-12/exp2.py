graph = {
'A': ['B', 'C'],
'B': ['A', 'C', 'D'],
'C': ['A', 'B', 'D'],
'D': ['B', 'C']
}
color_table={}
n=len(graph)
def color_graph(node):
    colors=set()
    for neighbour_node in graph[node]:
        if neighbour_node in color_table:
            colors.add(color_table[neighbour_node])
    for i in range(n):
        if i not in colors:
            color_table[node]=i
            break

        
for node in graph.keys():
    if node not in color_table:
        color_graph(node)

print(color_table)
print(max(color_table.values))
