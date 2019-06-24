library(tidyverse)

mini_iris <- iris[c(1, 51, 101), ]
gather(mini_iris, key = flower_att, value = measurement, Sepal.Length, Sepal.Width, Petal.Length, Petal.Width)

# expect-output-to-have: 1      setosa Sepal.Length         5.1