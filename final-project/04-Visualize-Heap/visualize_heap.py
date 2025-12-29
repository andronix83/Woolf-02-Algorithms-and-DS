import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def draw_heap(heap_array):
    """
    Converts an array representation of a heap into a tree structure
    and visualizes it.
    """
    if not heap_array:
        return

    # Step 1: Create a Node object for every element in the heap array
    nodes = [Node(val) for val in heap_array]

    # Step 2: Link nodes based on heap index properties
    for i, current_node in enumerate(nodes):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(nodes):
            current_node.left = nodes[left_index]

        if right_index < len(nodes):
            current_node.right = nodes[right_index]

    # The first element is always the root of the heap
    root = nodes[0]

    # Step 3: Visualize
    draw_tree(root)


def main() -> None:
    min_heap_array = [0, 4, 1, 5, 10, 3, 2]

    print("Visualizing Heap:", min_heap_array)
    draw_heap(min_heap_array)


if __name__ == "__main__":
    main()