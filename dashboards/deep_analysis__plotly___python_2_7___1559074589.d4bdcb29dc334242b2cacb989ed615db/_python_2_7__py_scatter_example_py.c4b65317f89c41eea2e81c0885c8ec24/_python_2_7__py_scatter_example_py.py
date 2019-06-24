# Based on https://plot.ly/python/line-and-scatter/
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Generate an 11 point sine curve
x = list(np.arange(1, 3.2, 0.2))
y = list(6 * np.sin(x))

# Create scatter plot from sine curve
t = go.Scatter(x=x, y=y, marker={'color': 'blue', 'size': 10}, mode='markers', name='t1')
layout = go.Layout(title="Scatter Plot", xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
data = go.Data([t])

# Output to UI
fig = go.Figure(data=data, layout=layout)
periscope.plotly(fig)
