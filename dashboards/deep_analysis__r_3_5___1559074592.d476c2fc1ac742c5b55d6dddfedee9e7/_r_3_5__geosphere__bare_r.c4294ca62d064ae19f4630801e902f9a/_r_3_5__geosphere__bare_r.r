# Based on https://cran.r-project.org/web/packages/geosphere/geosphere.pdf

library(geosphere)

alongTrackDistance(c(0,0),c(60,60),c(50,40))

# expect-output-to-have: 6627576
