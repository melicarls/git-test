library(RSQLite)
library(DBI)
library(dplyr)

con <- DBI::dbConnect(RSQLite::SQLite(), ":memory:")
copy_to(con, mtcars)
DBI::dbListTables(con)

# expect-output-to-have: Error
