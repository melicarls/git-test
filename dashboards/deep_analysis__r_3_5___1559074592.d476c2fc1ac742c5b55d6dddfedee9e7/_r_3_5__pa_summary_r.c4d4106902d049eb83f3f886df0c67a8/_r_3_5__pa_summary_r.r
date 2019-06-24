# Based on https://cran.r-project.org/web/packages/pa/pa.pdf

library(pa)

## Multi-period brinson analysis
data(quarter)
p2 <- brinson(x = quarter, date.var = "date", cat.var = "sector", bench.weight = "benchmark", portfolio.weight = "portfolio", ret.var = "return")

summary(p2)

# expect-output-to-have: Avg securities in the portfolio
