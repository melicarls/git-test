# Based on https://plot.ly/r/heatmap-webgl/
library(plotly)

# Use heatmapgl > heatmap for Web GL mode
p <- plot_ly(z = volcano, type = "heatmapgl")

# Output to UI
periscope.plotly(p)
