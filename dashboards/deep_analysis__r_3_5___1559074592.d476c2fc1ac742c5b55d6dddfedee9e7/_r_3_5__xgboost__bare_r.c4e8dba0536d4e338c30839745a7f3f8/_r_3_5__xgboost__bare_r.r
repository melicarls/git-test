# Based on https://cran.r-project.org/web/packages/xgboost/vignettes/xgboostPresentation.html

library(xgboost)

data(agaricus.train, package='xgboost')
data(agaricus.test, package='xgboost')
train <- agaricus.train
test <- agaricus.test

str(train)

# expect-output-to-have: List of 2
