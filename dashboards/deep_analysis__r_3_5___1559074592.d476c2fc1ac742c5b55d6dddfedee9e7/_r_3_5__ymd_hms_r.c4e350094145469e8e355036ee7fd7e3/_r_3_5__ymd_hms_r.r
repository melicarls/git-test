library(lubridate)

x <- c("2010-04-14-04-35-59", "2010-04-01-12-00-00")
ymd_hms(x)

# expect-output-to-have: "2010-04-14 04:35:59 UTC" "2010-04-01 12:00:00 UTC"
