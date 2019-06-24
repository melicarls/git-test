library(stringr)

fruit <- c("apple", "banana", "pear", "pinapple")
str_detect(fruit, "a$")

# expect-output-to-have: FALSE  TRUE FALSE FALSE
