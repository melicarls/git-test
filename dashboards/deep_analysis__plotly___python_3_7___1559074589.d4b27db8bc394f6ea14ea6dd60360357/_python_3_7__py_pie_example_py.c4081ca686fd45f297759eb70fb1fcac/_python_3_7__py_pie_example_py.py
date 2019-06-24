# Based on https://plot.ly/python/pie-charts/
import plotly.graph_objs as go
import pandas as pd
import numpy as np

labels = ['x1', 'x2', 'x3', 'x4']
values = [50, 500, 100, 500]
t = go.Pie(labels=labels, values=values)
layout = go.Layout(title="Basic Pie Chart")
data = go.Data([t])

# Output to UI
fig = go.Figure(data=data, layout=layout)
periscope.plotly(fig)
