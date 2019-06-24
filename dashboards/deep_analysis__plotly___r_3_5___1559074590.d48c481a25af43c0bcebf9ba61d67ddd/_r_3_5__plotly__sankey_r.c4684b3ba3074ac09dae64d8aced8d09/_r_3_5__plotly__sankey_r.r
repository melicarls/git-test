# Based on https://plot.ly/r/sankey-diagram/
library(plotly)

# Generate a sankey diagram of blue nodes and orange flows
p <- plot_ly(
    type = "sankey",
    orientation = "h",

    node = list(
      label = c("A1", "A2", "B1", "B2", "C1", "C2"),
      color = c("blue", "blue", "blue", "blue", "blue", "blue"),
      pad = 15,
      thickness = 20,
      line = list(
        color = "black",
        width = 0.5
      )
    ),

    link = list(
      source = c(0,1,0,2,3,3),
      target = c(2,3,3,4,4,5),
      value =  c(8,4,2,8,4,2),
      color = 'orange'
    )
  ) %>% 
  layout(
    title = "Basic Sankey Diagram",
    font = list(
      size = 10
    )
)

# Output to UI
periscope.plotly(p)
