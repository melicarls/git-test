# Based on https://plot.ly/r/histograms/
library(plotly)

p <- plot_ly(alpha = 0.6) %>%
  add_histogram(x = ~rnorm(500)) %>%
  add_histogram(x = ~rnorm(500) + 1) %>%
  layout(barmode = "overlay")

periscope.plotly(p)
