# -----------------------------------------------------------------------------
# Name:         load_game_board
# Purpose:      
# 
# Author:       Fiona Ding
# Created:      5/1/18
# -----------------------------------------------------------------------------
import pandas as pd
import networkx as nx



list_file_name = os.path.join("game_board",
                              "Scotland_Yard_Board_List_Format.csv")

list_df = pd.read_csv(list_file_name)


def create_graph_from_adjacency_list():
    # Replace empty cells with -1
    edge_lists_df.replace('--', '-1', inplace=True)

    # Split each column of from a comma separated to a list
    edge_lists_df["Taxi"] = edge_lists_df["Taxi"].str.split(',')
    edge_lists_df["Bus"] = edge_lists_df["Bus"].str.split(',')
    edge_lists_df["Subway"] = edge_lists_df["Subway"].str.split(',')
    edge_lists_df["Boat"] = edge_lists_df["Boat"].str.split(',')


    # Convert each column of edges into a dictionary
    taxi_edges = pd.Series(edge_lists_df["Taxi"].values, index=edge_lists_df.Vertex)
    taxi_edges = taxi_edges.to_dict()
    for vertex, edges in taxi_edges.items():
        # For each edge list of a given vertex, convert from a list of strings
        # to a list of ints
        new_edges = [int(edge) for edge in edges]

        # Convert each edge into a sorted pair
        new_edges = [tuple(sorted((vertex, edge)))
                     for edge in new_edges
                     if edge != -1]

        # Return to a string
        new_edges = str(new_edges).strip('[]')

        # Replace dictionary value
        taxi_edges[vertex] = new_edges

    bus_edges = pd.Series(edge_lists_df["Bus"].values, index=edge_lists_df.Vertex)
    bus_edges = bus_edges.to_dict()
    for vertex, edges in bus_edges.items():
        # For each edge list of a given vertex, convert from a list of strings
        # to a list of ints
        new_edges = [int(edge) for edge in edges]

        # Convert each edge into a sorted pair
        new_edges = [tuple(sorted((vertex, edge)))
                     for edge in new_edges
                     if edge != -1]

        # Return to a string
        new_edges = str(new_edges).strip('[]')

        # Replace dictionary value
        bus_edges[vertex] = new_edges

    subway_edges = pd.Series(edge_lists_df["Subway"].values, index=edge_lists_df.Vertex)
    subway_edges = subway_edges.to_dict()
    for vertex, edges in subway_edges.items():
        # For each edge list of a given vertex, convert from a list of strings
        # to a list of ints
        new_edges = [int(edge) for edge in edges]

        # Convert each edge into a sorted pair
        new_edges = [tuple(sorted((vertex, edge)))
                     for edge in new_edges
                     if edge != -1]

        # Return to a string
        new_edges = str(new_edges).strip('[]')

        # Replace dictionary value
        subway_edges[vertex] = new_edges

    boat_edges = pd.Series(edge_lists_df["Boat"].values, index=edge_lists_df.Vertex)
    boat_edges = boat_edges.to_dict()
    for vertex, edges in boat_edges.items():
        # For each edge list of a given vertex, convert from a list of strings
        # to a list of ints
        new_edges = [int(edge) for edge in edges]

        # Convert each edge into a sorted pair
        new_edges = [tuple(sorted((vertex, edge)))
                     for edge in new_edges
                     if edge != -1]

        # Return to a string
        new_edges = str(new_edges).strip('[]')

        # Replace dictionary value
        boat_edges[vertex] = new_edges

    # Convert back to dataframe
    cols = []

    taxi_ser = pd.Series(taxi_edges)
    taxi_ser.name = "Taxi"
    cols.append(taxi_ser)

    bus_ser = pd.Series(bus_edges)
    bus_ser.name = "Bus"
    cols.append(bus_ser)

    subway_ser = pd.Series(subway_edges)
    subway_ser.name = "Subway"
    cols.append(subway_ser)

    boat_ser = pd.Series(boat_edges)
    boat_ser.name = "Boat"
    cols.append(boat_ser)

    pairs_df = pd.concat(cols, axis=1)

    pairs_df.index.name = "Vertex"

    pairs_df.replace('', '--', inplace=True)
