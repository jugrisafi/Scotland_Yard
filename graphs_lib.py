# Fiona Testing git
#returns a graph g, made up of a tuple of verts and edges
#it should properly format a vertex and edge list
def instantiateGraph(verts, edges):
    return 0

#this makes an adjacency list graph from an input file
#it assumes that the input file is a series of edges
#which are written as ordered pairs (x, y) where x < y
def makeGraphFromFile(inputFile):
    edgeList = makeEdgeListFromFile(inputFile)
    myGraph = []

    #set up the blank sets for each element of the edge list
    for e in edgeList:
        myGraph.append(set())

    #we add one more because we won't zero index our graph...we'll just keep the zero index "null"
    myGraph.append(set())

    for e in edgeList:
        myGraph[e[0]].add(e[1])

    return myGraph

#This takes in an input file of edges which follows the "canonical scheme"
#(edges are written as ordered pairs (x, y) where x < y)
# and returns a list of sets (or 2-tuples...I'm not sure which is best)
def makeEdgeListFromFile(inputFile):
    edgeList = []
    with open(inputFile, "r") as f:
        for s in f:
            nums = s.split(';')
            # Vertex, Taxi, Bus, Subway, Boat
            # remember to strip /", should they exist




    return edgeList


# add vertex v to graph g
def addVertex(g, v):
    g[0].append(v)

# add an edge between vertex v1 and v2 in graph g
def addEdge(g, v1, v2):
    g[1].append((v1, v2))

# remove vertex v from graph g. Note, this will remove all edges that have a terminus in v
def removeVertex(g, v):
    return 0

# remove an edge between vertex v1 and v2 in graph g. Note: removing all edges to a vertex will NOT remove the vertex
def removeEdge(g, e):
    g[1].remove(e)

# returns a text representation of all verticies in graph g
def textVerts(g):
    while 1:
        printStr = ""
        for x in g[0][:]:
            printStr = printStr + str(x) + ", "
        return printStr

# returns a text representation of edges in graph g
def textEdges(g):
    while 1:
        printStr = ""
        for x in g[1][:]:
            printStr = printStr + str(x) + ", "
        return printStr

# prints a list of verticies in g
def printVerts(g):
    print(textVerts(g))

# prints a list of edges in g
def printEdges(g):
    print(textEdges(g))

# prints a text version of graph g
def printGraph(g):
    print("The graph has the following:\nVerticies: " + textVerts(g) + "\nEdges: " + textEdges(g))

#returns minimum distance between v1 and v2 on graph g
def findDistance(g, v1, v2):
    return bfs(g, v1, v2, 0)

#runs breadth first search to return shortest distance between vert1 and vert2 on graph g
# a return value of 0 signifies that the verticies are not connected
# there is a running assumption that v1 < v2 always
# because edges have been entered with the lower number first
def bfs(g, v1, v2, ans):
    subGraph = g
    edgeList = edgesWithThisVert(g, v1)

    for e in edgeList:
        if v2 in e:
            return ans + 1
        else:
            removeEdge(subGraph, e)
            return bfs(subGraph,e[0], v2, ans + 1)
    return 0

#returns a list of edges in graph g that have vertex v
def edgesWithThisVert(g, v):
    finalList = []

    #first we check to make sure the vertex is in the graph
    if g[0].index(v) >= 0:
        for x in g[1][:]:
            if v in x:
                finalList.append(x)
    return finalList

# Start borrowed code: cf - https://startupnextdoor.com/dijkstras-algorithm-in-python-3/
import queue
from collections import namedtuple

Edge = namedtuple('Edge', ['vertex', 'weight'])


class GraphUndirectedWeighted(object):
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, source, dest, weight):
        assert source < self.vertex_count
        assert dest < self.vertex_count
        self.adjacency_list[source].append(Edge(dest, weight))
        self.adjacency_list[dest].append(Edge(source, weight))

    def get_edge(self, vertex):
        for e in self.adjacency_list[vertex]:
            yield e

    def get_vertex(self):
        for v in range(self.vertex_count):
            yield v


def dijkstra(graph, source, dest):
    q = queue.PriorityQueue()
    parents = []
    distances = []
    start_weight = float("inf")

    for i in graph.get_vertex():
        weight = start_weight
        if source == i:
            weight = 0
        distances.append(weight)
        parents.append(None)

    q.put(([0, source]))

    while not q.empty():
        v_tuple = q.get()
        v = v_tuple[1]

        for e in graph.get_edge(v):
            candidate_distance = distances[v] + e.weight
            if distances[e.vertex] > candidate_distance:
                distances[e.vertex] = candidate_distance
                parents[e.vertex] = v
                # primitive but effective negative cycle detection
                if candidate_distance < -1000:
                    raise Exception("Negative cycle detected")
                q.put(([distances[e.vertex], e.vertex]))

    shortest_path = []
    end = dest
    while end is not None:
        shortest_path.append(end)
        end = parents[end]

    shortest_path.reverse()

    return shortest_path, distances[dest]
