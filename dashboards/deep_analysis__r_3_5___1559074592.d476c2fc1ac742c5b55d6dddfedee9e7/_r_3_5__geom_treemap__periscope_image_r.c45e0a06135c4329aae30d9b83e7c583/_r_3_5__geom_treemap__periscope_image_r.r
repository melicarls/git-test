library(ggplot2)
library(treemapify)

img <- ggplot(G20, aes(area = gdp_mil_usd, fill = region, label = country)) + geom_treemap() + geom_treemap_text(grow = T, reflow = T, colour = "black") + facet_wrap( ~ econ_classification) + scale_fill_brewer(palette = "Set1") + theme(legend.position = "bottom")
periscope.image(img)

# expect-image
