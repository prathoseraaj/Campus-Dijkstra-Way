import streamlit as st
import heapq
from graph import graph
from coordinates import coordinates
import pandas as pd
import folium
import streamlit.components.v1 as components

def dijkstra(graph, start):
    
    distances ={node: float('inf') for node in graph}
    distances[start] = 0

    previous_nodes = {node: None for node in graph}

    pq = [(0, start)] #priority queue

    while pq :

        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes

def shortest_path(previous_nodes,end):

    path = []
    current = end
    while current is not None :
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    return path

# Streamlit App
st.title("Campus-Dijkstra-Way")

start_node = st.selectbox("Select the start point", list(graph.keys()))
end_node = st.selectbox("Select the destination", list(graph.keys()))

if st.button("Find Shortest Path"):
    if start_node and end_node:
        # Run Dijkstra's algorithm
        distances, previous_nodes = dijkstra(graph, start_node)

        # Get the shortest path
        path = shortest_path(previous_nodes, end_node)

        
        st.subheader(f"Shortest distance from {start_node} to {end_node} ")
        st.write(f"Distance: {distances[end_node]} m")

        st.subheader(f"Shortest Path:")
        st.write(" -> ".join(path))

        # Initialize Folium map for the selected path
        m = folium.Map(location=[12.641493, 77.436931], zoom_start=17)

        # Highlight the start and end points on the map with custom markers
        path_coordinates = []

        for node in path:
            lat, lon = coordinates[node]
            path_coordinates.append((lat, lon))
            folium.Marker([lat, lon], popup=f"{node}", icon=folium.Icon(color='green')).add_to(m)

        # Add line to connect the nodes in the path
        folium.PolyLine(
            locations=path_coordinates,
            color='red',
            weight=3,
            opacity=0.7
        ).add_to(m)

        # Generate HTML for the updated map
        map_html = m._repr_html_()

        # Display the updated map as an iframe
        components.html(map_html, height=500)