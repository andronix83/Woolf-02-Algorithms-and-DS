import networkx as nx
from collections import deque
import heapq


def bfs_path(graph: nx.Graph, start: str, goal: str):
    """
    Implements Breadth-First Search to find the shortest path (in edges).
    Uses a Queue (FIFO).
    """
    # Queue stores tuples: (current_node, path_to_current_node)
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        vertex, path = queue.popleft()  # Dequeue from the left (FIFO)

        if vertex == goal:
            return path

        if vertex not in visited:
            visited.add(vertex)
            # Add neighbors to queue
            for neighbor in graph.neighbors(vertex):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append((neighbor, new_path))
    return None


def dfs_path(graph: nx.Graph, start: str, goal: str):
    """
    Implements Depth-First Search.
    Uses a Stack (LIFO).
    """
    # Stack stores tuples: (current_node, path_to_current_node)
    stack = [(start, [start])]
    visited = set()

    while stack:
        vertex, path = stack.pop()  # Pop from the end (LIFO)

        if vertex == goal:
            return path

        if vertex not in visited:
            visited.add(vertex)
            # Add neighbors to stack
            neighbors = list(graph.neighbors(vertex))
            for neighbor in neighbors:
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append((neighbor, new_path))
    return None


def dijkstra_paths(graph: nx.Graph, start):
    """
    Implements Dijkstra's algorithm to find the shortest paths to all nodes.
    Uses a Priority Queue (Min-Heap).
    """
    # Dictionary to store the shortest distance to each node, initialized to infinity
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start] = 0

    # Dictionary to store the path (predecessor of each node)
    previous_nodes = {node: None for node in graph.nodes()}

    # Priority queue stores tuples: (current_distance, current_node)
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Optimization: If we found a shorter path to this node already, skip
        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes


def dijkstra_reconstruct_path(previous_nodes, start, goal):
    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        if current_node == start:
            break
        current_node = previous_nodes[current_node]
    return path[::-1]  # Reverse to get start -> goal
