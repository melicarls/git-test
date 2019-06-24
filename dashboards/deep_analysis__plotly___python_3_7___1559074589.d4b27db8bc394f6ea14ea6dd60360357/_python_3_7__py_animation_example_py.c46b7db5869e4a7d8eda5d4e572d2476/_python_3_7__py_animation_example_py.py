# Based on https://plot.ly/python/animations/
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Generate an 11 point sine curve
x = list(np.arange(1, 3.2, 0.2))
y = list(6 * np.sin(x))

# Create scatter plot from sine curve
t = go.Scatter(x=x, y=y, marker={'color': 'blue', 'size': 10}, mode='markers', name='t1')
layout = go.Layout(title="Scatter Plot",
                   xaxis={'title': 'x1', 'range': [0.5, 3.5], 'autorange': False},
                   yaxis={'title': 'x2', 'range': [0, 9], 'autorange': False},
                   updatemenus=[{'type': 'buttons',
                                 'buttons': [{'label': 'Play',  # Play button to animate plot
                                              'method': 'animate',
                                              'args': [None]}]}])
data = go.Data([t])
frames = go.Frames([{'data': [{'x': x[:i + 1], 'y': y[:i + 1]}]} for i in range(11)])

# Output to UI
fig = go.Figure(data=data, layout=layout, frames=frames)
periscope.plotly(fig)
