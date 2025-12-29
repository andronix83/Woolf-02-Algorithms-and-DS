import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Add node with its current color
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Binary Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def generate_color_gradient(n, start_hex, end_hex):
    # Convert hex to RGB tuples (0-1 range)
    c1 = mcolors.hex2color(start_hex)
    c2 = mcolors.hex2color(end_hex)

    gradient = []
    for i in range(n):
        # Linear interpolation
        alpha = i / (n - 1) if n > 1 else 0
        r = c1[0] + (c2[0] - c1[0]) * alpha
        g = c1[1] + (c2[1] - c1[1]) * alpha
        b = c1[2] + (c2[2] - c1[2]) * alpha
        # Convert back to hex
        gradient.append(mcolors.to_hex((r, g, b)))

    return gradient


# --- Traversal Algorithms ---

def get_dfs_order(root):
    if not root:
        return []
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        visited.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited


def get_bfs_order(root):
    if not root:
        return []

    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        visited.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited


def visualize_traversal(root, order_function, title, start_color="#1296F0", end_color="#E0F0FF"):
    # 1. Get the list of nodes in the specific order
    ordered_nodes = order_function(root)

    # 2. Generate gradient colors corresponding to the number of nodes
    total_nodes = len(ordered_nodes)
    colors = generate_color_gradient(total_nodes, start_color, end_color)

    # 3. Assign colors to nodes based on their position in the list
    for i, node in enumerate(ordered_nodes):
        node.color = colors[i]

    # 4. Draw the tree
    draw_tree(root, title=title)


def main() -> None:
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # 2. Visualize Depth-First Search (DFS)
    # Colors will flow from dark to light following the Depth-First path
    print("Visualizing DFS (Depth-First Search)...")
    visualize_traversal(root, get_dfs_order, "DFS Visualization (Dark=Start, Light=End)")

    # 3. Visualize Breadth-First Search (BFS)
    # Colors will flow from dark to light layer by layer
    print("Visualizing BFS (Breadth-First Search)...")
    visualize_traversal(root, get_bfs_order, "BFS Visualization (Dark=Start, Light=End)")


if __name__ == "__main__":
    main()