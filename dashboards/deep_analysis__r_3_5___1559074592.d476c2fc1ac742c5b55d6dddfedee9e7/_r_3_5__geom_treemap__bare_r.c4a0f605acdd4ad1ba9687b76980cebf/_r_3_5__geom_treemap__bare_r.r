library(ggplot2)
library(treemapify)

ggplot(G20, aes(area = gdp_mil_usd, fill = hdi, label = country)) + geom_treemap() + geom_treemap_text(fontface = "italic", colour = "white", place = "centre", grow = TRUE)

# expect-image
