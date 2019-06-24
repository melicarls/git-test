# Based on https://plot.ly/r/line-charts/ 
library(plotly)
p <- plot_ly(x = 1:10, y = 1:10, type="scatter", mode="markers")

# Output to UI
periscope.plotly(p)
