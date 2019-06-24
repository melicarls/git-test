# Based on https://plot.ly/python/box-plots/
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# Generate a random histogram
x1 = np.random.randn(50)
x2 = np.random.randn(50) + 1

t1 = go.Histogram(x=x1, opacity=0.75)
t2 = go.Histogram(x=x2, opacity=0.75)
layout = go.Layout(title="Histogram", barmode='overlay', xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
data = go.Data([t1, t2])

# Output to UI
fig = go.Figure(data=data, layout=layout)
periscope.plotly(fig)
