from graphics import *
from graphs_lib import *


def main():
    # some random operations that should be added to a main function later on

    vertexList = []
    edgeList = []
    graph = [vertexList, edgeList]

    for x in range(5):
        addVertex(graph, x)

    addEdge(graph, 1, 2)
    addEdge(graph, 2, 3)
    addEdge(graph, 3, 4)
    addEdge(graph, 3, 5)

    printGraph(graph)

    print("The distance between verticies 1 and 3 is " + str(findDistance(graph, 1, 3)))

    g = GraphUndirectedWeighted(5)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 1)
    g.add_edge(2, 3, 1)
    g.add_edge(2, 4, 1)

    shortest_path, distance = dijkstra(g, 0, 2)
    assert shortest_path == [0, 1, 2] and distance == 2

    #
    # win = GraphWin('Draw a Triangle', 350, 350)
    # # win.yUp()  # right side up coordinates
    # win.setBackground('yellow')
    # message = Text(Point(win.getWidth()/2, 30), 'Click on three points')
    # message.setTextColor('red')
    # message.setStyle('italic')
    # message.setSize(20)
    # message.draw(win)
    #
    # # Get and draw three vertices of triangle
    # p1 = win.getMouse()
    # p1.draw(win)
    # p2 = win.getMouse()
    # p2.draw(win)
    # p3 = win.getMouse()
    # p3.draw(win)
    # vertices = [p1, p2, p3]
    #
    # # Use Polygon object to draw the triangle
    # triangle = Polygon(vertices)
    # triangle.setFill('gray')
    # triangle.setOutline('cyan')
    # triangle.setWidth(4)  # width of boundary line
    # triangle.draw(win)
    #
    # message.setText('Click anywhere to quit') # change text message
    # win.getMouse()
    # win.close()


main()
