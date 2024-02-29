import osmnx as ox
import geopy.distance
import re  
import pdb

def clean_speeds(road_map):
    #edge is the code for each road
    for edge in road_map.edges:
    # Cleaning the "maxspeed" attribute, some values are lists, some are strings, some are None
        maxspeed = 40
        #road_map.edge[edge] is the value for each road that contains the all the data for the road
        if "maxspeed" in road_map.edges[edge]:
            maxspeed = road_map.edges[edge]["maxspeed"]
            if type(maxspeed) == list:
                speeds = [ int(speed) for speed in maxspeed ]
                maxspeed = min(speeds)
            elif type(maxspeed) == str:
                if 'mph' in maxspeed:
                    
                    maxspeed = int(maxspeed.replace('mph', ''))
                    maxspeed = round(maxspeed * 0.277778)
                maxspeed = int(maxspeed)
        road_map.edges[edge]["maxspeed"] = maxspeed
        # Adding the "weight" attribute (time = distance / speed)
        road_map.edges[edge]["weight"] = road_map.edges[edge]["length"] / maxspeed
    pdb.set_trace()
                    
    return road_map

def style_unvisited_edge(edge, road_map):        
    road_map.edges[edge]["color"] = "#d36206"
    road_map.edges[edge]["alpha"] = 0.2
    road_map.edges[edge]["linewidth"] = 0.5

def style_visited_edge(edge, road_map):
    road_map.edges[edge]["color"] = "#d36206"
    road_map.edges[edge]["alpha"] = 1
    road_map.edges[edge]["linewidth"] = 1

def style_active_edge(edge, road_map):
    road_map.edges[edge]["color"] = '#e8a900'
    road_map.edges[edge]["alpha"] = 1
    road_map.edges[edge]["linewidth"] = 1

def style_path_edge(edge, road_map):
    road_map.edges[edge]["color"] = "white"
    road_map.edges[edge]["alpha"] = 1
    road_map.edges[edge]["linewidth"] = 1



# Configure OSMnx
ox.config(use_cache=True, log_console=True)

# Define your start and end points (latitude, longitude)
start_point = (9.962582, -84.188251)
end_point = (9.838837, -83.945967)

# Calculate the bounding box that includes both points
north = max(start_point[0], end_point[0])
south = min(start_point[0], end_point[0])
east = max(start_point[1], end_point[1])
west = min(start_point[1], end_point[1])

# Convert 10 km extension to degrees approximately (rough estimation)
# Note: This is a simplification and works better for small distances and not too close to the poles.
km_in_degree = 1 / 111  # Roughly 111 km per degree
extension_degree = 10 * km_in_degree

# Extend the bounding box
north += extension_degree
south -= extension_degree
east += extension_degree
west -= extension_degree

# Download the extended street network
road_map = ox.graph_from_bbox(north, south, east, west, network_type='drive')

road_map = clean_speeds(road_map)
road_map = style_unvisited_edge(road_map)
road_map = style_visited_edge(road_map)
road_map = style_active_edge(road_map)
road_map = style_path_edge(road_map)




# Plot the graph

fig, ax = ox.plot_graph(ox.project_graph(road_map))