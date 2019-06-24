# Based on https://cran.r-project.org/web/packages/zoo/zoo.pdf

library(zoo)

## averaging over values in a month:
# x.date is jan 1,3,5,7; feb 9,11,13; mar 15,17,19
x.date <- as.Date(paste(2004, rep(1:4, 4:1), seq(1,20,2), sep = "-")); x.date
x <- zoo(rnorm(12), x.date); x

plot(x)

# expect-image
