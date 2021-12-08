# import usefull packages
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import nxviz as nv
import seaborn as sns
import csv
import pandas as pd
# from nxviz import GeoPlot
# CRIANDO GRAFO  
df_airports = pd.read_csv('airports.csv')
df_flights = pd.read_csv('anac.csv')

G = nx.Graph()

# Add nodes
for index, row in df_airports.iterrows():
    G.add_node(row['code'],
              name=row['name'],
              country=row['country'],
              latitude=float(row['lat_geo_point'].replace(",",".")),
              longitude=float(row['lon_geo_point'].replace(",",".")),
              region=row['region']
              )

# Add edges
df_edges = df_flights[[
    'origin_airport_abbreviation',
    'destination_airport_abbreviation',
]].dropna()
df_edges = df_edges.groupby(df_edges.columns.tolist(), as_index=False).size()
for index, row in df_edges.iterrows():
    if row['origin_airport_abbreviation'] == row['destination_airport_abbreviation']:
        continue
    G.add_edge(row['origin_airport_abbreviation'], row['destination_airport_abbreviation'], flight_count=row['size'])

# Export to graphml
nx.write_graphml(G, 'air_traffic.graphml')
print("sucesso!")