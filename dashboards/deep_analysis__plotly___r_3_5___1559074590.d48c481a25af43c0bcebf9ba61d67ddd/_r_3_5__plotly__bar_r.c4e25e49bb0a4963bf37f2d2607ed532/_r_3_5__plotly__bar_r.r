# Based on https://plot.ly/r/bar-charts/
library(plotly)
p <- plot_ly(
  x = c("x1", "x2", "x3"),
  y = c(10, 20, 50),
  type = "bar"
)

# Output to UI
periscope.plotly(p)
