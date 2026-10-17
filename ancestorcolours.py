##
## =======================================================
## Jialu Sun
## CS 231 Spring 2025
## Assignment 1, P2
## =======================================================
##

from trees import Tree
import check

def ancestor_colours(tree, choice):
    """
    ancestor_colours(tree, choice) produces a list of strings of colours of ancestors
    of the node with ID choice in tree. The output is in order from the parent of the node
    up through to the root.
    
    ancestor_colours: Tree Str -> (listof Str)
    
    Examples:
    Sample tree 3
    
    ancestor_colours(tree, "c") => ["blue", "red"]
    ancestor_colours(tree, "a") => []
    """
    colours = []
    parent = tree.parent(choice)
    
    while parent is not None:
        colours.append(tree.node_colour(parent))
        parent = tree.parent(parent)
    
    return colours

# sample tree 3
tree3 = Tree()
tree3.add_root("a")
tree3.set_node_weight("a", 3)
tree3.set_node_colour("a", "red")
tree3.add_leaf("a", "b")
tree3.set_node_weight("b", 10)
tree3.set_node_colour("b", "blue")
tree3.add_leaf("b", "d")
tree3.set_node_weight("d", 20)
tree3.set_node_colour("d", "blue")
tree3.add_leaf("a", "c")
tree3.set_node_weight("c", 4)
tree3.set_node_colour("c", "green")
tree3.add_leaf("c", "e")
tree3.set_node_weight("e", 5)
tree3.set_node_colour("e", "red")
tree3.add_leaf("c", "f")
tree3.set_node_weight("f", 6)
tree3.set_node_colour("f", "blue")

# Test 1: Ancestors of node "e"
check.expect("Q2T1", ancestor_colours(tree3, "e"), ["green", "red"])

# Test 2: Ancestors of node "a" (root)
check.expect("Q2T2", ancestor_colours(tree3, "a"), [])

# Test 3: Ancestors of node "d"
check.expect("Q2T3", ancestor_colours(tree3, "d"), ["blue", "red"])

# Test 4: Ancestors of node "f"
check.expect("Q2T4", ancestor_colours(tree3, "f"), ["green", "red"])

# Test 5: Ancestors of node "b"
check.expect("Q2T5", ancestor_colours(tree3, "b"), ["red"])