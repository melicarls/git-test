# Based on https://plot.ly/python/heatmaps/
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Generate a heatmap
z = [[1, 20, 30],
     [20, 1, 60],
     [30, 60, 1]]
x = [1, 2, 3]
y = [1, 2, 3]

t = go.Heatmap(x=x, y=y, z=z)
layout = go.Layout(title="Heatmap", xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
data = go.Data([t])

# Output to UI
fig = go.Figure(data=data, layout=layout)
periscope.plotly(fig)
