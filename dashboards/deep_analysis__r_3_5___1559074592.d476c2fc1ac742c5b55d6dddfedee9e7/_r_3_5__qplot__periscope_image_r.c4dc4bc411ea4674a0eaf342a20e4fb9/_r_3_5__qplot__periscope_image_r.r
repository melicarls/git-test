library(ggplot2)
p <- qplot(mpg, wt, data = mtcars)
periscope.image(p)

# expect-image
