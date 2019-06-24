library(reshape2)

names(airquality) <- tolower(names(airquality))
aqm <- melt(airquality, id = c("month", "day"), na.rm = TRUE)

library(plyr)
acast(aqm, variable ~ month, mean, subset = .(variable == "ozone"))

# expect-output-to-have: ozone 23.61538 29.44444 59.11538 59.96154 31.44828
