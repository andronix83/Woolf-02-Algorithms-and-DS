import heapq


def dijkstra(graph, start_node):
    """
    Implements Dijkstra's algorithm using a binary heap (priority queue).
    """

    # Initialize distances to all nodes as infinity, except the start node
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0

    # Priority queue to store tuples of (current_distance, current_node)
    # Using a min-heap ensures we always process the closest node next
    priority_queue = [(0, start_node)]

    while priority_queue:
        # Pop the node with the smallest distance from the heap
        current_distance, current_node = heapq.heappop(priority_queue)

        # Optimization: If we found a shorter path to this node already, skip processing
        if current_distance > distances[current_node]:
            continue

        # Iterate over neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Push the new shorter distance to the priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def main() -> None:
    # Graph definition: A weighted directed graph
    # Format: 'Node': {'Neighbor': Weight}
    graph_example = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_vertex = 'A'
    shortest_paths = dijkstra(graph_example, start_vertex)

    print(f"Shortest paths from {start_vertex}:")
    for node, distance in shortest_paths.items():
        print(f"To {node}: {distance}")


if __name__ == "__main__":
    main()