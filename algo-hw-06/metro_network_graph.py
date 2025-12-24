import networkx as nx
import matplotlib.pyplot as plt

import algorithms as alg


# ==========================================
# TASK 1: Graph Creation and Visualization
# ==========================================

def create_kyiv_metro_graph():
    G = nx.Graph()

    # Define lines as lists of stations (ordered)
    # Line M1 (Sviatoshynsko-Brovarska) - Red color
    line_m1 = [
        "Akademmistechko", "Zhytomyrska", "Sviatoshyn", "Nyvky",
        "Beresteiska", "Shuliavska", "Politekhnichnyi Instytut",
        "Vokzalna", "Universytet", "Teatralna", "Khreshchatyk",
        "Arsenalna", "Dnipro", "Hidropark", "Livoberezhna",
        "Darnytsia", "Chernihivska", "Lisova"
    ]

    # Line M2 (Obolonsko-Teremkivska) - Blue color
    line_m2 = [
        "Heroiv Dnipra", "Minska", "Obolon", "Pochaina",
        "Tarasa Shevchenka", "Kontraktova Ploshcha", "Poshtova Ploshcha",
        "Maidan Nezalezhnosti", "Ploshcha Ukrainskykh Heroiv",
        "Olimpiiska", "Palats 'Ukraina'", "Lybidska",
        "Demiivska", "Holosiivska", "Vasylkivska",
        "Vystavkovyi Tsentr", "Ipodrom", "Teremky"
    ]

    # Line M3 (Syretsko-Pecherska) - Green color
    line_m3 = [
        "Syrets", "Dorohozhychi", "Lukianivska", "Zoloti Vorota",
        "Palats Sportu", "Klovska", "Pecherska", "Zvirynetska",
        "Vydubychi", "Slavutych", "Osokorky", "Pozniaky",
        "Kharkivska", "Vyrlytsia", "Boryspilska", "Chervonyi Khutir"
    ]

    # Add nodes and edges for each line
    for i in range(len(line_m1) - 1):
        G.add_edge(line_m1[i], line_m1[i+1], weight=2) # standard travel time - 2 min
        G.nodes[line_m1[i]]['line'] = 'red'
    G.nodes[line_m1[-1]]['line'] = 'red'

    for i in range(len(line_m2) - 1):
        G.add_edge(line_m2[i], line_m2[i+1], weight=2)
        G.nodes[line_m2[i]]['line'] = 'blue'
    G.nodes[line_m2[-1]]['line'] = 'blue'

    for i in range(len(line_m3) - 1):
        G.add_edge(line_m3[i], line_m3[i+1], weight=2)
        G.nodes[line_m3[i]]['line'] = 'green'
    G.nodes[line_m3[-1]]['line'] = 'green'

    # Define Hubs (Transfer stations)
    # Connecting the lines physically and marking nodes as hubs
    transfers = [
        ("Teatralna", "Zoloti Vorota"),                     # Red - Green
        ("Khreshchatyk", "Maidan Nezalezhnosti"),           # Red - Blue
        ("Ploshcha Ukrainskykh Heroiv", "Palats Sportu")    # Blue - Green
    ]

    hub_stations = []
    for u, v in transfers:
        G.add_edge(u, v, weight=5) # Transfer takes longer (e.g., 5 min)
        hub_stations.extend([u, v])
        G.nodes[u]['type'] = 'hub'
        G.nodes[v]['type'] = 'hub'

    return G, hub_stations


def show_kyiv_metro_graph(G, hubs):
    # Visualization setup
    plt.figure(figsize=(14, 10))

    # Simplified layout (Topology approximation)
    pos = nx.kamada_kawai_layout(G)

    # Determine colors for nodes
    color_map = []
    for node in G.nodes():
        if node in hubs:
            color_map.append('gold') # Hubs get a special color
        else:
            # Fallback to line color
            color_map.append(G.nodes[node].get('line', 'gray'))

    # Draw the graph
    nx.draw(G, pos, node_color=color_map, with_labels=True,
            node_size=500, font_size=8, font_color='black', edge_color='gray')

    plt.title("Kyiv Metro Visualization")
    plt.show()


def analyze_graph(G):
    # Graph Analysis
    print("-" * 30)
    print("TASK 1: Graph Analysis")
    print("-" * 30)
    print(f"Number of nodes (Stations): {G.number_of_nodes()}")
    print(f"Number of edges (Connections): {G.number_of_edges()}")

    # Degree of vertices (connections per station)
    # Listing top 5 most connected stations (hubs usually have degree 3 or 4)
    degrees = sorted(G.degree, key=lambda x: x[1], reverse=True)
    print("\nTop 5 stations by connections (Degree):")
    for station, degree in degrees[:6]:
        print(f"{station}: {degree}")


# ==========================================
# TASK 2: BFS vs DFS Paths
# ==========================================

def bfs_vs_def_paths(G, start_station, end_station):
    print("\n" + "-" * 30)
    print("TASK 2: BFS vs DFS Paths")
    print("-" * 30)

    bfs_path = alg.bfs_path(G, start_station, end_station)
    dfs_path = alg.dfs_path(G, start_station, end_station)

    print(f"Start: {start_station} -> End: {end_station}")
    print(f"\nBFS Path ({len(bfs_path)} steps): {bfs_path}")
    print(f"DFS Path ({len(dfs_path)} steps): {dfs_path}")


# ==========================================
# TASK 3: Dijkstra Algorithm
# ==========================================

def dijkstra_paths(G, start_station, end_station):
    print("\n" + "-" * 30)
    print("TASK 3: Dijkstra Shortest Path (Weighted)")
    print("-" * 30)

    # Calculate weighted shortest path using Dijkstra
    # Weights were added during graph creation:
    # - Travel between stations: 2 units
    # - Transfer between lines: 5 units

    dijkstra_distances, previous = alg.dijkstra_paths(G, start_station)
    dijkstra_path = alg.dijkstra_reconstruct_path(previous, start_station, end_station)

    print(f"Dijkstra Path (Weighted): {dijkstra_path}")
    print(f"Total 'Time' (Weight): {dijkstra_distances[end_station]} minutes")

    # Example for finding the shortest paths between ALL nodes (showing subset)
    print("\nShortest paths from 'Khreshchatyk' to all other nodes (subset):")
    all_paths = nx.single_source_dijkstra_path(G, source="Khreshchatyk", weight='weight')
    for target in ["Lisova", "Teremky", "Syrets"]:
        print(f"To {target}: {all_paths[target]}")


def main():
    # Instantiate Graph
    G, hubs = create_kyiv_metro_graph()

    # Configure and Show Graph
    show_kyiv_metro_graph(G, hubs)

    analyze_graph(G)

    start_station = "Heroiv Dnipra"
    end_station = "Chervonyi Khutir"

    bfs_vs_def_paths(G, start_station, end_station)

    dijkstra_paths(G, start_station, end_station)


if __name__ == "__main__":
    main()