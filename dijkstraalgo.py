import heapq
# source = 'A'  # Define the starting node (source)
 #   target = 'E'  # Define the destination node (target)
  #  distances, predecessors = dijkstra(graph, weights, source)
def dijkstra(graph, weights, source):
    
    distances ={node: float('inf') for node in graph}
    distances[source] = 0

    predecessors = {node: None for node in graph}

    priority_queue = [(0, source)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor in graph[current_node]:
            edge_weight = weights[(current_node, neighbor)]
            new_distance = current_distance + edge_weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node

                heapq.heappush(priority_queue, (new_distance, neighbor))
    return distances, predecessors

graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E'],
        'E': ['C', 'D']
    }

    # Step 2: Define the edge weights
    # Edge weights are represented as a dictionary where the key is a tuple (u, v)
    # and the value is the weight of the edge between u and v
weights = {
        ('A', 'B'): 1,
        ('A', 'C'): 4,
        ('B', 'A'): 1,
        ('B', 'C'): 2,
        ('B', 'D'): 5,
        ('C', 'A'): 4,
        ('C', 'B'): 2,
        ('C', 'D'): 1,
        ('C', 'E'): 3,
        ('D', 'B'): 5,
        ('D', 'C'): 1,
        ('D', 'E'): 2,
        ('E', 'C'): 3,
        ('E', 'D'): 2
    }

    # Step 3: Call the Dijkstra function
source = 'A'  # Define the starting node (source)
target = 'E'  # Define the destination node (target)
distances, predecessors = dijkstra(graph, weights, source) 

print(distances)