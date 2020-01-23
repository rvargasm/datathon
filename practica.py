#Práctica de introducción a redes.
import networkx as nx
import matplotlib.pyplot as plt

D = nx.DiGraph()
D.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K',
				'L', 'M', 'N', 'O'])
D.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('C', 'A'), ('D', 'E'), ('D', 'B'),
				('B', 'E'), ('E', 'C'), ('E','D'), ('A', 'E'), ('A','N'), ('N','O'), ('N','L'),
				('O','L'), ('L','M'), ('K','L'), ('K','M'), ('O','K'), ('G', 'A'),('O', 'J'),
				('J', 'O'), ('F','G'),('H','G'),('I','G'),('G','A'),('I','H'),('H','I'),
				('I','J'),('I','F'),('G','J'),('J','F')])
#print(D.nodes())
nx.draw(D, with_labels = True)
plt.show()
print(len(D.edges()))
