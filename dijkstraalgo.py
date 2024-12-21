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



graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1, 'E': 3},
        'D': {'B': 5, 'C': 1, 'E': 2},
        'E': {'C': 3, 'D': 2}
    }

start_node = 'A'  # Starting node
end_node = 'E'    # Destination node

    # Run Dijkstra's algorithm
distances, previous_nodes = dijkstra(graph, start_node)

print("Distances:", distances)