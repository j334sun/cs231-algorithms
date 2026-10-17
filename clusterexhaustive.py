##
## =======================================================
## Jialu Sun
## CS 231 Spring 2025
## Assignment 1, P3
## =======================================================
##
from graphs import *
import check

def generate_combinations(arr, n, start, index, combination, result):
    """
    generate_combinations(arr, n, start, index, combination, result) generate combinations recursively.

    generate_combinations: (listof X) Int Int Int (listof X) (listof (listof X)) -> None
    """
    if index == n:
        result.append(combination[:])
        return
    for i in range(start, len(arr)):
        combination[index] = arr[i]
        generate_combinations(arr, n, i + 1, index + 1, combination, result)

def get_combinations(arr, n):
    """
    get_combinations(arr, n) generates all combinations of n elements from the list arr.
    
    get_combinations: (listof X) Int -> (listof (listof X))
    """
    result = []
    combination = [0] * n
    generate_combinations(arr, n, 0, 0, combination, result)
    return result

def cluster_exhaustive(graph, size):
    """
    cluster_exhaustive(graph, size) produces the minimum total value of any cluster
    of size size in the given non-empty graph. If no such cluster exists, returns 0.
    
    cluster_exhaustive: Graph Int -> Int
    
    Examples:
    Using sample graph 2:
    cluster_exhaustive(graph, 2) => 5
    Using sample graph 4:
    cluster_exhaustive(graph, 4) => 111
    """
    vertices = graph.vertices()
    if size <= 1 or size > len(vertices):
        return 0
    
    min_value = None
    found_cluster = False
    
    combinations = get_combinations(vertices, size)
    
    for cluster in combinations:
        total_value = 0
        is_cluster = True
        for i in range(len(cluster)):
            for j in range(i + 1, len(cluster)):
                if not graph.are_adjacent(cluster[i], cluster[j]):
                    is_cluster = False
                    break
                total_value += graph.edge_weight(cluster[i], cluster[j])
            if not is_cluster:
                break
        if is_cluster:
            found_cluster = True
            if min_value is None or total_value < min_value:
                min_value = total_value
    
    return min_value if found_cluster else 0


graph2 = make_graph("samplegraph2.txt")
# Test 1: Cluster of size 2 on graph 2
check.expect("Q3T1", cluster_exhaustive(graph2, 2), 5)

# Test 2: Cluster of size 4 on graph 2
check.expect("Q3T2", cluster_exhaustive(graph2, 4), 111)

# Test 3: Cluster of size 0 on graph 2
check.expect("Q3T3", cluster_exhaustive(graph2, 0), 0)

# Test 4: Cluster of size 1 on graph 2
check.expect("Q3T4", cluster_exhaustive(graph2, 1), 0)

# Test 5: Cluster of size 6 (larger than number of vertices)
check.expect("Q3T5", cluster_exhaustive(graph2, 6), 0)