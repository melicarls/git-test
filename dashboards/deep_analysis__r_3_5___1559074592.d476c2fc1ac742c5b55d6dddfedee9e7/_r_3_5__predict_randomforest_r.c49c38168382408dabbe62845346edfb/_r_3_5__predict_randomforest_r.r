library(randomForest)

set.seed(111)
ind <- sample(2, nrow(iris), replace = TRUE, prob=c(0.8, 0.2))
iris.rf <- randomForest(Species ~ ., data=iris[ind == 1,])
predict(iris.rf, iris[ind == 2,])

# expect-output-to-have: Levels: setosa versicolor virginica
