# Based on https://plot.ly/python/box-plots/
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Generate random data for box plot
x1 = np.random.randn(50)
x2 = np.random.randn(50) + 1

t1 = go.Box(x=x1, opacity=0.75)
t2 = go.Box(x=x2, opacity=0.75)
layout = go.Layout(title="Box", barmode='overlay', xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
data = go.Data([t1, t2])

# Output to UI
fig = go.Figure(data=data, layout=layout)
periscope.plotly(fig)
