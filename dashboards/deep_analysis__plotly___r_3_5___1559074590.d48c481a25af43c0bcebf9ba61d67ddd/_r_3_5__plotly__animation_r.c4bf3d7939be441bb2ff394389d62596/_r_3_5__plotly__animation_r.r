# Based on https://plot.ly/r/animations/
library(plotly)

# Draw a triangle across three frames
df <- data.frame(
  x = c(1,2,3), 
  y = c(1,2,1), 
  f = c(1,2,3)
)

p <- df %>%
  plot_ly(
    x = ~x,
    y = ~y,
    frame = ~f,
    type = 'scatter',
    mode = 'markers',
    showlegend = F
  ) 

# Output to UI
periscope.plotly(p)
