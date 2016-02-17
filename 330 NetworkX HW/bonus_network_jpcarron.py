__author__ = 'Joer'

import networkx as nx
import json
from networkx.readwrite import json_graph

# Generate the graph above
g = nx.read_dot("imdb_actors_graph.dot")

degree = nx.degree_centrality(g)

betweenness = nx.betweenness_centrality(g, normalized=True)


closeness = nx.closeness_centrality(g)

##################SORT#################

sorted_degree = sorted(degree.items(), reverse=True, key = lambda x: x[1])
print('degree: ' + str(sorted_degree[:10]))

sorted_betweenness = sorted(betweenness.items(), reverse=True, key= lambda x: x[1])
print('betweenness: ' + str(sorted_betweenness[:10]))

sorted_closeness = sorted(closeness.items(), reverse=True,key= lambda x: x[1])
print ('closeness: ' + str(sorted_closeness[:10]))

print "+++++++++++++++++++"

g1 = nx.read_dot("imdb_actors_graph.dot")
g1.add_edges_from([("Harrison Ford", "Brad Pitt"), ("Brad Pitt", "Natalie Portman")])

degree1 = nx.degree_centrality(g1)

betweenness1 = nx.betweenness_centrality(g1, normalized=True)

closeness1 = nx.closeness_centrality(g1)

nx.write_gml(g1, "imdb_actors_graph_modified.json")

###############SORT################

sorted_degree1 = sorted(degree1.items(), reverse=True, key = lambda x: x[1])
print('degree1: ' + str(sorted_degree1[:10]))

sorted_betweenness1 = sorted(betweenness1.items(), reverse=True, key= lambda x: x[1])
print('betweenness1: ' + str(sorted_betweenness1[:10]))

sorted_closeness1 = sorted(closeness1.items(), reverse=True,key= lambda x: x[1])
print ('closeness1: ' + str(sorted_closeness1[:10]))

from networkx.readwrite import json_graph
data = json_graph.node_link_data(g1)

H = json_graph.node_link_graph(data)

for n in g1:
    g1.node[n]['name'] = n
# write json formatted data
d = json_graph.node_link_data(g1) # node-link format to serialize
# write json
json.dump(d, open('imdb_actors_graph_modified.json','w'))
print('\n' + 'Wrote node-link JSON data to imdb_actors_graph_modified.json')
# open URL in running web browser