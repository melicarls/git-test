# Based on https://cran.r-project.org/web/packages/pa/pa.pdf

library(pa)

data(jan)
## Single-period brinson analysis
p1 <- brinson(x = jan, date.var = "date", cat.var = "sector", bench.weight = "benchmark", portfolio.weight = "portfolio", ret.var = "return")

exposure(p1, var = "sector")
plot(p1, var = "sector", type = "exposure")

# expect-image
