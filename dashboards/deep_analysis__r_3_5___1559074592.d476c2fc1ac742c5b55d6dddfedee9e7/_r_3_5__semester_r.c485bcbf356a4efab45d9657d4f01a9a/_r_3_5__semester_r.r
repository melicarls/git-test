library(lubridate)

x <- ymd(c("2012-03-26", "2012-05-04", "2012-09-23", "2012-12-31"))
semester(x, with_year = TRUE)

# expect-output-to-have: 2012.1 2012.1 2012.2 2012.2
