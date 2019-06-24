library(plotly)
library(dplyr)
set.seed(123)

df <- diamonds[sample(1:nrow(diamonds), size = 1000),]

df.summ <- df %>% group_by(cut) %>% summarize(Mean = mean(table), Min = min(table), Max = max(table))

p <- ggplot(df.summ, aes(x = cut, y = Mean, ymin = Min, ymax = Max, fill = cut)) + geom_bar(stat = "identity") + geom_errorbar() + ggtitle("Bar chart with Error Bars")

p <- ggplotly(p)

periscope.plotly(p)

# expect-plotly
# expect-output-to-have: Bar chart with Error Bars
