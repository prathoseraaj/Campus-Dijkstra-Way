import heapq

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


graph = {
    'Jain University Gate': {'Golf course': 100, 'Short-cut near Non IT building': 350},
    'Golf course': {'Jain University Gate': 100, 'FET (MAIN)': 300},
    'FET (MAIN)': {'Golf course': 300, 'FET (BACK)': 97},
    'FET (BACK)': {'FET (MAIN)': 97, 'Mess': 44, 'Himalayas': 63},
    'Himalayas': {'FET (BACK)': 63, 'Mess': 71},
    'Mess': {'FET (BACK)': 44, 'Himalayas': 71, 'Purvanchal': 71},
    'Purvanchal': {'Mess': 71, 'Karakoram': 39},
    'Karakoram': {'Purvanchal': 39, 'Football field': 160},
    'Football field': {'Karakoram': 160, 'Tennis court': 98},
    'Tennis court': {'Football field': 98, 'Sprintoor': 180, 'Sai Baba temple': 180},
    'Sprintoor': {'Tennis court': 180, 'Swimming Pool': 54},
    'Swimming Pool': {'Sprintoor': 54},
    'Sai Baba temple': {'Tennis court': 180, 'Non IT building': 250},
    'Colosseum': {'Sai Baba temple': 130},
    'Short-cut near Non IT building': {'Jain University Gate': 350, 'Non IT building': 120, 'Football field': 240},
    'Non IT building': {'Short-cut near Non IT building': 120, 'Sai Baba temple': 250}
}


start_node = input("START POINT: ")  # Starting node
end_node = input("DESTINATION: ")    # Destination node

    # Run Dijkstra's algorithm
distances, previous_nodes = dijkstra(graph, start_node)

print("Distances:", distances)
print("Previous nodes:", previous_nodes)

print(f"Shortest distance from {start_node} to {end_node}: {distances[end_node]}")
print(f"Path: {' -> '.join(shortest_path(previous_nodes, end_node))}")
