library(reshape2)

names(airquality) <- tolower(names(airquality))
aqm <- melt(airquality, id = c("month", "day"), na.rm = TRUE)

dcast(aqm, month ~ variable, mean, margins = c("month", "variable"))

# expect-output-to-have: 1     5 23.61538 181.2963 11.622581 65.54839 68.70696
