library(caret)

featurePlot(x = iris[, 1:4], y = iris$Species, plot = "ellipse", auto.key = list(columns = 3))

# expect-image
