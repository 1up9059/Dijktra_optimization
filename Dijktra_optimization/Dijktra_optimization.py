import pdb

import osmnx as ox
import random
import heapq
import networkx as nx

def style_unvisited_edge(edge):        
    G.edges[edge]["color"] = "#d36206"
    G.edges[edge]["alpha"] = 0.2
    G.edges[edge]["linewidth"] = 0.5

def style_visited_edge(edge):
    G.edges[edge]["color"] = "#d36206"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def style_active_edge(edge):
    G.edges[edge]["color"] = '#e8a900'
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def style_path_edge(edge):
    G.edges[edge]["color"] = "white"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1



#place_name_1 = "Santa Ana, San José, Costa Rica"
#place_name_2 = "El Guarco, Cartago, Costa Rica"
#G1 = ox.graph_from_place(place_name_1, network_type="drive")
#G2 = ox.graph_from_place(place_name_2, network_type="drive")
#pdb.set_trace()
#combined_graph = nx.compose(G1, G2)
#ox.plot_graph(combined_graph)
