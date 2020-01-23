import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()
g.add_edges_from([('F','G'),('H','G'),('I','G'),('G','A'),('I','H'),('H','I'),('I','J'),('I','F'),('G','J'),('J','F')])
nx.draw(g, with_labels=True)
