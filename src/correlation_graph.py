"""
correlation_graph.py

Creates and visualizes a correlation graph between financial assets using NetworkX and matplotlib.
Only relationships with high correlation (> 0.8) are shown as edges in the graph.

Real-Life Use Case:
Used by quant researchers and risk teams to understand dependency networks between stocks.
Overconnected assets may indicate concentration risk or co-movement patterns during market volatility.

Core Concepts:
- Graph representation of asset correlation
- Visualization for network interpretation
"""

"""
Correlation Graph of Assets using NetworkX

Models correlation relationships between stocks using an undirected graph.
"""

from typing import Set, Tuple
import networkx as nx
import matplotlib.pyplot as plt


AssetPair = Tuple[str, str]


def build_correlation_graph(edges: Set[AssetPair]) -> nx.Graph:
    G = nx.Graph()
    G.add_edges_from(edges)
    return G


def visualize_graph(G: nx.Graph, title: str = "Correlation Network") -> None:
    pos = nx.spring_layout(G, seed=42)  # Deterministic layout
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        edge_color="gray",
        node_size=1600,
        font_size=10
    )
    plt.title(title)
    plt.tight_layout()
    plt.show()


def main():
    correlated_pairs: Set[AssetPair] = {
        ("AAPL", "MSFT"),
        ("GOOGL", "MSFT"),
        ("TSLA", "NVDA"),
        ("AAPL", "NVDA"),
    }

    graph = build_correlation_graph(correlated_pairs)
    visualize_graph(graph)


if __name__ == "__main__":
    main()
