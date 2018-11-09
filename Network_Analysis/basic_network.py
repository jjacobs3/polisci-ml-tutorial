import networkx as nx

# Create graph
cool_graph = nx.Graph()
cool_graph.add_node(1)
cool_graph.add_node(2)
cool_graph.add_node(3)
cool_graph.add_edge(1,2)
cool_graph.add_edge(2,3)
print(cool_graph.nodes())
print(cool_graph.edges())

# Display graph
import matplotlib.pyplot as plt
nx.draw_spring(cool_graph, with_labels=True)
plt.show()

nx.write_adjlist(cool_graph,"adj.txt", data=True)
nx.write_edgelist(cool_graph,"edges.txt")