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

import networkx as nx
import matplotlib.pyplot as plt

# Define correlations > 0.8
correlations = {
    ("AAPL", "MSFT"),
    ("GOOGL", "MSFT"),
    ("TSLA", "NVDA"),
    ("AAPL", "NVDA"),
}

G = nx.Graph()
G.add_edges_from(correlations)

# Visualize
nx.draw(G, with_labels=True, node_color="lightgreen", node_size=2000, font_size=10)
plt.title("High Correlation Network")
plt.show()
