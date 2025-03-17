from matching import Graph, greedy_algorithm, make_directed_graph, find_path, find_maximum_matching, get_endpoints
import pytest
import copy

#Initializing graph for testing

myG = Graph()
myG.add_node("Alice")
myG.add_node("Bob")
myG.add_node("Carol")
myG.add_node("CS170")
myG.add_node("CS200")
myG.add_node("CS500")
myG.add_edge("Alice170", "Alice", "CS170")
myG.add_edge("Alice200", "Alice", "CS200")
myG.add_edge("Bob170", "Bob", "CS170")
myG.add_edge("Carol500", "Carol", "CS500")
C = {"CS170", "CS200", "CS500"}
S = {"Alice", "Bob", "Carol"}


def test_make_directed_graph():
    myG_copy = copy.deepcopy(myG)
    newG: Graph = make_directed_graph(myG_copy, set(), C, S)
    assert ("Alice170") in newG.edges
    assert ("Alice200") in newG.edges
    assert ("Bob170") in newG.edges
    assert ("Carol500") in newG.edges
    assert ("Alice") in newG.nodes
    assert ("Bob") in newG.nodes
    assert ("Carol") in newG.nodes
    assert ("CS170") in newG.nodes
    assert ("CS200") in newG.nodes
    assert ("CS500") in newG.nodes



def test_augmenting_path_simple():
    #Tests that the correct augmenting path is found for the partial matching which would be produced by the greedy algorithm.
    M = set()
    M.add(("Alice170"))
    M.add(("Carol500"))
    myG_copy = copy.deepcopy(myG)
    newG = make_directed_graph(myG_copy, M, C, S)
    augmenting_path = find_path(newG, "s", "t", set())
    assert augmenting_path == [('s-Bob', True), ('Bob170', False), ('Alice170', False), ('Alice200', False), ('CS200-t', True)]

def test_find_maximum_matching():
    #Tests that the maxmimum matching (matching each HTA to a Course) is correctly returned
    myG_copy = copy.deepcopy(myG)
    matching = find_maximum_matching(myG_copy, C, S)
    assert ("Alice200") in matching
    assert ("Carol500") in matching
    assert ("Bob170") in matching

