import csv
from pathlib import Path
from typing import List

import networkx as nx

from DegreeCentrality.degree import create_graph, typed_deal, degree_statistical


def process_degree(G, variables):
    nodes = []
    degree_centrality = nx.degree_centrality(G)
    for i in range(0, len(variables)):
        nodes.append((variables[i],degree_centrality[i]))

    nodes.sort(key=lambda line: line[1], reverse=True)
    return [Path(x[0]) for x in nodes]


def recommend_by_degree(rate: float, dependency_url) -> List[Path]:
    G, variables, edge_list = create_graph(dependency_url)

    sorted_nodes = process_degree(G, variables)
    top_k_nodes = sorted_nodes[:int(rate * len(sorted_nodes))]
    return [var for var in top_k_nodes]


def recommend_by_drh(drh_url, rate: float) -> List[Path]:
    pass


def recommend_by_maintenance(proj: Path, rate: float) -> List[Path]:
    pass
