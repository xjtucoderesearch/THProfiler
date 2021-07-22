import csv
from pathlib import Path
from typing import List

import networkx as nx

from DegreeCentrality.degree import create_graph, typed_deal, degree_statistical


def process_degree(G, variables, typed_url):
    typed, dictionary = typed_deal(typed_url)
    node_result = range(0, G.number_of_nodes())
    degree_centrality, degree_temp_ratio, degree_typed_ratio = degree_statistical(nx.degree_centrality(G), variables,
                                                                                  typed, dictionary)

    node_columns = ["NodeID", "Nodename", "degree_centrality"]
    with open("node_url", 'w', newline='') as t_file:
        csv_writer = csv.writer(t_file)
        csv_writer.writerow(node_columns)
        for l in range(len(node_result)):
            csv_writer.writerow([node_result[l], variables[l], '%.4f' % degree_centrality[l]])
    nodes = [[node_result[l], variables[l], degree_centrality[l]] for l in range(len(node_result))]

    nodes.sort(key=lambda line: line[2])
    return nodes



def recommend_by_degree(rate: float, dependency_url, file_type_url) -> List[Path]:
    G, variables, edge_list = create_graph(dependency_url)

    sorted_nodes = process_degree(G, variables, file_type_url)
    top_k_nodes = sorted_nodes[:int(rate * len(sorted_nodes))]
    return [Path(var) for id,var,degree_centrality  in top_k_nodes]

def recommend_by_drh(rate: float, dependency_url, file_type_url) -> List[Path]:
    pass
