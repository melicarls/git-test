library(tidyr)

unite_(mtcars, "vs_am", c("vs","am"))

# expect-output-to-have: vs_am
