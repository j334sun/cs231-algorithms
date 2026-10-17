##
## =======================================================
## Jialu Sun
## CS 231 Spring 2024
## Assignment 4, P1
## =======================================================
##

from graphs import Graph
import check

def is_cluster(graph, vertices):
    """
    is_cluster(graph, vertices) checks if the given set of vertices forms a cluster (complete subgraph).
    Returns True if the set of vertices are, False otherwise.
    
    is_cluster: Graph (listof Str) -> Bool
    
    Examples:
    
    is_cluster(graph, ["A", "B", "C"]) => True
    is_cluster(graph, ["A", "F"]) => False
    """
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            if not graph.are_adjacent(vertices[i], vertices[j]):
                return False
    return True

def find_max_cluster(graph, current_cluster, vertices, max_cluster):
    """
    find_max_cluster(graph, current_cluster, vertices, max_cluster) recursively finds and returns 
    the largest cluster using backtracking.
    
    find_max_cluster: Graph (listof Str) (listof Str) (listof Str) -> None
    
    Examples:
    sample graph 1
    
    find_max_cluster(graph, ["A"], ["B", "C", "D"], ["A", "B", "C"]) => None
    """
    if is_cluster(graph, current_cluster):
        if len(current_cluster) > len(max_cluster):
            max_cluster.clear()
            max_cluster.extend(current_cluster)
    
    for i in range(len(vertices)):
        new_cluster = current_cluster + [vertices[i]]
        remaining_vertices = vertices[i + 1:]
        find_max_cluster(graph, new_cluster, remaining_vertices, max_cluster)

def cluster_backtrack(graph):
    """
    cluster_backtrack(graph) is a shell function that calls the recursive function
    find_max_cluster, which finds the largest cluster in the given graph using backtracking.
    
    cluster_backtrack: Graph -> (listof Str)
    
    Examples:
    graph = sample graph 2 below
    
    cluster_backtrack(graph) => ["A", "B", "C", "D", "E"]
    """
    vertices = graph.vertices()
    max_cluster = []
    find_max_cluster(graph, [], vertices, max_cluster)
    return max_cluster

# testing zone

graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")

largest_cluster = cluster_backtrack(graph)
# Test 1
check.expect("Largest cluster in graph1", set(largest_cluster), {"A", "B", "C"})

graph2 = Graph()
graph2.add_vertex("A")
graph2.add_vertex("B")
graph2.add_vertex("C")
graph2.add_vertex("D")
graph2.add_vertex("E")
graph2.add_vertex("F")
graph2.add_vertex("G")
graph2.add_vertex("H")
graph2.add_edge("A", "B")
graph2.add_edge("A", "C")
graph2.add_edge("A", "D")
graph2.add_edge("A", "E")
graph2.add_edge("B", "C")
graph2.add_edge("B", "D")
graph2.add_edge("B", "E")
graph2.add_edge("C", "D")
graph2.add_edge("C", "E")
graph2.add_edge("D", "E")
graph2.add_edge("E", "F")
graph2.add_edge("F", "G")
graph2.add_edge("F", "H")
graph2.add_edge("G", "H")

largest_cluster_2 = cluster_backtrack(graph2)
# Test 2
check.expect("Largest cluster in graph2", set(largest_cluster_2), {"A", "B", "C", "D", "E"})

# larger graph
graph3 = Graph()
graph3.add_vertex("A")
graph3.add_vertex("B")
graph3.add_vertex("C")
graph3.add_vertex("D")
graph3.add_vertex("E")
graph3.add_vertex("F")
graph3.add_edge("A", "B")
graph3.add_edge("A", "C")
graph3.add_edge("B", "C")
graph3.add_edge("D", "E")
graph3.add_edge("E", "F")
graph3.add_edge("D", "F")

largest_cluster3 = cluster_backtrack(graph3)
# Test 3
check.expect("Largest cluster in graph3:", set(largest_cluster3), {"A", "B", "C"}) 

# graph with no edges
graph4 = Graph()
graph4.add_vertex("A")
graph4.add_vertex("B")
graph4.add_vertex("C")

largest_cluster4 = cluster_backtrack(graph4)
# Test 4
check.expect("Largest cluster in graph4:", set(largest_cluster4), {"A"})

# fully connected graph
graph5 = Graph()
graph5.add_vertex("A")
graph5.add_vertex("B")
graph5.add_vertex("C")
graph5.add_vertex("D")
graph5.add_edge("A", "B")
graph5.add_edge("A", "C")
graph5.add_edge("A", "D")
graph5.add_edge("B", "C")
graph5.add_edge("B", "D")
graph5.add_edge("C", "D")

largest_cluster5 = cluster_backtrack(graph5)
# Test 5
check.expect("Largest cluster in graph5:", set(largest_cluster5), {"A", "B", "C", "D"}) 