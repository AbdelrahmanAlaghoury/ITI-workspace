# In[23]:
import networkx as nx
# In[24]:


graph = {
    '0':['1', '3', '8'],
    '1':['0', '7'],
    '2':['3', '5', '7'],
    '3':['0', '2', '4'],
    '4':['3', '8'],
    '5':['2', '6'],
    '6':['5'],
    '7':['1', '2'],
    '8':['0', '4']
}

G =nx.Graph(graph)
nx.draw(G, with_labels = True)
print("BFS ----> ", list(nx.bfs_tree(G, source='0')))
print("BFS_edges ----> ", nx.bfs_tree(G, source='0').edges)
print("=======================================================================================================================")
print("DFS ----> ", list(nx.dfs_tree(G, source='0')))
print("DFS_edges ----> ", nx.dfs_tree(G, source='0').edges)
print("=======================================================================================================================")
print("Dijkstra_path ----> ", nx.dijkstra_path(G, source='0', target='6'))
print("=======================================================================================================================")


# In[26]:


import matplotlib.pyplot as plt
graph = {
    '0': ['2','1'],
    '1': ['0','6','5','3'],
    '2': ['5','6','0'],
    '3': ['1','7'],
    '4': ['6','7'],
    '5': ['2','7','1'],
    '6': ['2','1','7','4'],
    '7': ['4','6','5','3'],
    }

G = nx.Graph(graph)

G.add_edge('0','1',weight=8)
G.add_edge('0','2',weight=9)
G.add_edge('1','3',weight=1)
G.add_edge('1','5',weight=7)
G.add_edge('1','6',weight=9)
G.add_edge('2','5',weight=6)
G.add_edge('2','6',weight=4)
G.add_edge('3','7',weight=4)
G.add_edge('4','7',weight=7)
G.add_edge('5','7',weight=2)
G.add_edge('6','7',weight=6)

pos = nx.spring_layout(G)
nx.draw(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels, font_weight='bold')
plt.axis("off")
plt.show()
print("Dijkstra_path ----> ", nx.dijkstra_path(G, source='0', target='6'))


# In[ ]:




