library(randomForest)

rf <- randomForest(mpg ~ ., mtcars, keep.forest = FALSE, ntree = 100)
p <- plot(rf, log = "y")
periscope.image(p)

# expect-image
