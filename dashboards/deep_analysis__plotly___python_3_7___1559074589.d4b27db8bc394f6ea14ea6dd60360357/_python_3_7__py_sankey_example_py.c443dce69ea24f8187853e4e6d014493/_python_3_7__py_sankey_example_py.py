# Based on https://plot.ly/python/sankey-diagram/
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Create sankey diagram with blue nodes and orange flows
t = go.Sankey(
    node=dict(
        label=["A1", "A2", "B1", "B2", "C1", "C2"],
        color=["blue", "blue", "blue", "blue", "blue", "blue"],
    ),
    link=dict(  # flow arrows params
        source=[0, 1, 0, 2, 3, 3],
        target=[2, 3, 3, 4, 4, 5],
        value=[8, 4, 2, 8, 4, 2],
        color='orange'
    ))

layout = go.Layout(title="Basic Sankey Diagram")
data = go.Data([t])

# Output to UI
fig = go.Figure(data=data, layout=layout)
periscope.plotly(fig)
