# Based on https://plot.ly/python/bar-charts/
import plotly.graph_objs as go
import pandas as pd
import numpy as np

t = go.Bar(x=['x1', 'x2', 'x3'], y=[10, 15, 30])
layout = go.Layout(title="Bar Chart", xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
data = go.Data([t])

# Output to UI
fig = go.Figure(data=data, layout=layout)
periscope.plotly(fig)
