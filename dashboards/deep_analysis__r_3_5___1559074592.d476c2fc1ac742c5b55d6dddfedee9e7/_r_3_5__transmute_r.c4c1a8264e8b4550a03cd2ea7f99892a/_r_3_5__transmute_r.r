library(dplyr)

mtcars %>% transmute(displ_l = disp / 61.0237)

# expect-output-to-have: displ_l
# expect-output-to-have: 1  2.621932
