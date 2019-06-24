library(datasets)
library(tibble)
library(dplyr)

t <- as_tibble(iris)
nrow(distinct(t))

# expect-output-to-have: 149
