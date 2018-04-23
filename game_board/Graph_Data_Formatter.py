# -----------------------------------------------------------------------------
# Name:         Graph_Data_Formatter
# Purpose:      
# 
# Author:       Fiona Ding
# Created:      4/7/18
# -----------------------------------------------------------------------------
import os
import pandas as pd


def temp_converter():
    df = pd.read_csv("Scotland_Yard_Graph_partial.csv")

    df["Taxi Edges"] = df["Taxi Edges"].str.replace('[()]', '')

    df["Taxi Edges"] = df["Taxi Edges"].str.split(',')

    # df["Taxi Edges"] = df["Taxi Edges"].

    taxi = pd.Series(df['Taxi Edges'].values, index=df.Vertex)

    taxi.to_csv('delete-taxi.csv')


    df["Bus Edges"] = df["Bus Edges"].str.replace('[()]', '')

    df["Bus Edges"] = df["Bus Edges"].str.split(',')

    bus = pd.Series(df['Bus Edges'].values, index=df.Vertex)

    bus.to_csv('delete-bus.csv')


    df["Underground Edges"] = df["Underground Edges"].str.replace('[()]', '')

    df["Underground Edges"] = df["Underground Edges"].str.split(',')

    bus = pd.Series(df['Underground Edges'].values, index=df.Vertex)

    bus.to_csv('delete-underground.csv')

    #
    # df2 = df.loc[~df["Taxi Edges"].isnull(), 'Taxi Edges']


def convert_pairs_to_lists(edge_pairs):
    """
    Convert edge_pairs from a list of ordered pairs into a list of adjacent
    neighbors.

    Args:
        edge_pairs:

    Returns:

    """
    pass


def convert_lists_to_pairs(edge_lists):
    """
    Convert edge_lists from a list of adjacent neighbors to a list of ordered
    pairs.

    Args:
        edge_lists:

    Returns:

    """
    # Replace empty cells with -1
    edge_lists.replace('--', '-1', inplace=True)

    # Split each column of from a comma separated to a list
    edge_lists["Taxi"] = edge_lists["Taxi"].str.split(',')
    edge_lists["Bus"] = edge_lists["Bus"].str.split(',')
    edge_lists["Subway"] = edge_lists["Subway"].str.split(',')
    edge_lists["Boat"] = edge_lists["Boat"].str.split(',')



    # Convert each column of edges into a dictionary
    taxi_edges = pd.Series(edge_lists["Taxi"].values, index=edge_lists.Vertex)
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

    bus_edges = pd.Series(edge_lists["Bus"].values, index=edge_lists.Vertex)
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

    subway_edges = pd.Series(edge_lists["Subway"].values, index=edge_lists.Vertex)
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

    boat_edges = pd.Series(edge_lists["Boat"].values, index=edge_lists.Vertex)
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

    pairs_df.fillna('--', inplace=True)

    return pairs_df



def check_graph(edge_list):
    """
    Double check for typos, etc by looking for any uni-directional edges.
    (Since the game board is an undirected graph.)

    Args:
        edge_list:

    Returns:

    """
    pass



if __name__ == '__main__':
    list_file_name = os.path.join("game_board",
                                  "Scotland_Yard_Board_List_Format.csv")

    list_df = pd.read_csv(list_file_name)

    out_df = convert_lists_to_pairs(list_df)

    out_df.to_csv(os.path.join("game_board",
                               "Scotland_Yard_Board_Pairs_Format.csv"))

