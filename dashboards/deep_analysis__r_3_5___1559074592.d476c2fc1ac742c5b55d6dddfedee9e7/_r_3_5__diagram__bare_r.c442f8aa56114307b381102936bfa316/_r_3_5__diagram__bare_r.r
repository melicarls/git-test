# Based on https://cran.r-project.org/web/packages/diagram/diagram.pdf

library(diagram)

openplotmat(main = "bentarrow")
pos <- cbind( A <- seq(0.1, 0.9, by = 0.2), rev(A))
text(pos, LETTERS[1:5], cex = 2)

for (i in 1:4)
  bentarrow(from = pos[i,] + c(0.05, 0), to = pos[i+1,] + c(0, 0.05), arr.pos = 1, arr.adj = 1)

# expect-image
