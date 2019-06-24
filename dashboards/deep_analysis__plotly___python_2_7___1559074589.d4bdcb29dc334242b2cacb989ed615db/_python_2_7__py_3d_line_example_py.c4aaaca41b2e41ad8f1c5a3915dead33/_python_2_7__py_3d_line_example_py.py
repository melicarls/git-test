# Based on https://plot.ly/python/3d-line-plots/
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Generate an 11 point sine curve in 3 dimensions
x = list(np.arange(1, 3.2, 0.2))
y = list(6 * np.sin(x))
z = list(np.arange(0, 11, 1))

# Create line graph including markers from sine curve
t = go.Scatter3d(x=x, y=y, z=z, marker={'color': 'blue', 'size': 10}, mode='lines+markers', name='t1')
layout = go.Layout(title="3D Line Graph", scene=go.Scene(xaxis={'title': 'x1'}, yaxis={'title': 'x2'}, zaxis={'title': 'x3'}))
data = go.Data([t])

# Output to UI
fig = go.Figure(data=data, layout=layout)
periscope.plotly(fig)
