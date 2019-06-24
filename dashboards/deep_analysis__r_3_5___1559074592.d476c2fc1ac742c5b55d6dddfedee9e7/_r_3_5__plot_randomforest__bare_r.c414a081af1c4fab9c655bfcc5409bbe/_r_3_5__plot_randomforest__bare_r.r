library(randomForest)

rf <- randomForest(mpg ~ ., mtcars, keep.forest = FALSE, ntree = 100)
plot(rf, log = "y")

# expect-image
