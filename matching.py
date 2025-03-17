class Graph:
    def __init__(self):
        self.nodes, self.edges = [], []
        self.dart2head, self.head2darts = dict(), dict()
    def add_node(self, node):
        self.nodes.append(node)
        self.head2darts[node] = []
    def add_edge(self, edge, tail, head):
        "When interpreting graph as directed, arc is directed from tail to head"
        self.edges.append(edge)
        dart_true = (edge, True)
        dart_false = (edge, False)
        self.dart2head[dart_true] = head
        self.dart2head[dart_false] = tail
        self.head2darts[head].append(dart_true)
        self.head2darts[tail].append(dart_false)

def dart2edge(d):
    return d[0]

def rev(d):
    "returns the dart with same edge as d but in reverse of d's direction"
    return (d[0],not d[1])

def get_endpoints(G, edge):
    return G.dart2head[(edge, True)], G.dart2head[(edge, False)]
    
def make_directed_graph(G: Graph, M: dict, C: set, S: set):
    G_arrow = Graph()
    for node in G.nodes:
        G_arrow.add_node(node)
    # Now iterate over all edges. For each edge in G,
    # add a correctly "oriented" edge to G_arrow based on whether a node is in C or S and whether it is matched or not. 
    # refer to March 12th lecture notes!

    ### TODO: Fill in here

    ###

    #Now, we add our new nodes to allow for a single call to find_path on G_arrow to yield any augmenting path in G
    G_arrow.add_node("s")
    G_arrow.add_node("t")
    for node in S:
        # unmatched?
        if not any(dart2edge(dart) in M for dart in G.head2darts[node]):
            G_arrow.add_edge("s-"+str(node), "s", node)
    for node in C:
        # unmatched?
        if not any(dart2edge(dart) in M for dart in G.head2darts[node]):
            G_arrow.add_edge(str(node)+"-t", node, "t")
    return G_arrow

def find_path(G: Graph, s, t, A: set):
    "return an s-to-t path that avoids A if one exists, else None"

    return NotImplementedError("missing code in find_path")

def augment_matching(M, augmenting_path):
    "augment the matching M along the given augmenting path"

    return NotImplementedError("missing code in augment_matching")

    
def find_maximum_matching(G, C, S):
    M = set()
    return NotImplementedError("missing code in find_maximum_matching")

# Here is an example graph you can use!
        
myG = Graph()
myG.add_node(1)
myG.add_node(2)
myG.add_node(3)
myG.add_node(4)
myG.add_edge("12", 1, 2)
myG.add_edge("14", 1, 4)
myG.add_edge("23", 2, 3)
# Draw this graph
# Make sure find_path works
C = {1,3}
S = {2,4}
out = find_maximum_matching(myG, C, S)

