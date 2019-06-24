library(data.table)

DT = data.table(ID = c("b","b","b","a","a","c"), a = 1:6, b = 7:12, c = 13:18)
DT

# expect-output-to-have: b 1  7 13
