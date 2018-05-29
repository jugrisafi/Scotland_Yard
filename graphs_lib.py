# Fiona Testing git
# returns a graph g, made up of a tuple of verts and edges
# it should properly format a vertex and edge list
def instantiateGraph(verts, edges):
    return 0

# this makes an adjacency list graph from an input file
# it assumes that the input file is a series of edges
# which are written as ordered pairs (x, y) where x < y
def makeGraphFromFile(inputFile):
    edgeList = makeEdgeListFromFile(inputFile)
    myGraph = []

    # set up the blank sets for each element of the edge list
    for e in edgeList:
        myGraph.append(set())

    # we add one more because we won't zero index our graph...we'll just keep the zero index "null"
    myGraph.append(set())

    for e in edgeList:
        myGraph[e[0]].add(e[1])

    return myGraph

# This takes in an input file of edges which follows the "canonical scheme"
# (edges are written as ordered pairs (x, y) where x < y)
# and returns a list of sets (or 2-tuples...I'm not sure which is best)
def makeEdgeListFromFile(inputFile):
    edgeList = []
    with open(inputFile, "r") as f:
        for s in f:
            nums = s.split(';')
            # Vertex, Taxi, Bus, Subway, Boat
            # remember to strip /", should they exist

    return edgeList

# This takes in a graph in the form of an adjacency list, and
# returns a graph in the form of an adjacency matrix.
def makeAdjacencyMatrixFromAdjacencyList(adjacencyList):
    # first, we set up the matrix and set all entries to 0
    matrix = [[0 for i in range(len(adjacencyList)+1)] for j in range(len(adjacencyList)+1)]

    # next, we'll set all entries in row 0 and column 0 to -2,
    # since those values are off limits (we're not zero indexing our verticies)
    # and we'll set all entries of [x][x] to -1
    for i in range(len(matrix)+1):
        matrix[i][i] = -1
        matrix[0][i] = -2
        matrix[i][0] = -2

    # finally, we read in each edge from the list, and properly enter it into the matrix
    for v1 in adjacencyList:
        for v2 in v1:
            matrix[v1][v2] = 1
            # if all protocols of our graph data have been followed, this line is redundant
            # (because the data should always have v1<v2,)
            # but we're adding it here just in case, since it doesn't really hurt us in run time
            matrix[v2][v1] = 1

    # and we return the completed matrix
    return matrix

# This function takes in an adjacencyMatrix representation of a graph
# and it then fills in all 0's with the minimum distance between those nodes
# a writeup of the algorithm is forthcoming
def setMinimumDistances(graph, adjacencyList):
    counter = 1
    anyZeros = True

    while(anyZeros):
        anyZeros = False
        for i in range(len(graph)+1):
            for j in range(i+1):
                # first, we'll do a check to see if the data is a zero
                # ...if, so, we set anyZeros back to true to make sure we "scan" the graph again
                if graph[i][j] == 0:
                    anyZeros = True

                # next, we do the actual work of changing values in our matrix
                # by induction, we only need to worry about values equal to the current
                # value of our counter variable
                if graph[i][j] == counter:
                    # we look at all verticies directly connected to i,
                    # and update their distance to j to be counter + 1 if they are not
                    # already connected to j (by a shorter route)
                    for v in adjacencyList[i]:
                        # check to make sure we're following the standard form where pairs of verticies are
                        # always considered with the lowest first
                        if v < j:
                            if graph[v][j] == 0:
                                graph[v][j] = counter + 1
                        # if v > j, then we want to make sure we index with j first, since we're always
                        # trying to keep ordered pairs with the smaller vertex number as the first
                        else:
                            if graph[j][v] == 0:
                                graph[j][v] = counter + 1

        counter += 1
    # end while

    # finally, we "copy" our data from the "upper half" of the adjacency matrix
    # to the "lower half." This may be considered strange, given the desire
    # to always keep vertex pairs as (lower, higher), but
    # when it comes to the AI playing the game, it will save the step
    # of needing to do a conditional every time a distance is checked
    for i in range(len(graph)+1):
        for j in range(i+1):
            # we want to ignore the zero column and row, plus the main diagonal
            # since the code above only exits the while loop when no zeros exist, the strict
            # inequality is sufficient
            if graph[i][j] > 0:
                # we'll do two checks for errors...this is because I'm being a little paranoid
                # about the fact that I will not look through all 40,000 values by hand to see if they are right
                # first, we'll check to make sure all edges have been properly preserved
                if graph[i][j] == 1 and graph[j][i] != 1:
                    raise UserWarning("Matrix data has been corrupted. Upper half edge not found in lower half.")
                # second, we'll make sure that the lower half didn't get any stray data
                if graph[i][j] != 1 and graph[j][i] != 0:
                    raise UserWarning("Matrix data has been corrupted. Lower half contains unexpected data.")
                graph[j][i] = graph[i][j]

    return graph

# returns minimum distance between v1 and v2 on graph g
def findDistance(gAdjacencyMatrix, v1, v2):
    return gAdjacencyMatrix[v1][v2]
