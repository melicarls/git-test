library(plotly)

dat1 <- data.frame(sex = factor(c("Female","Female","Male","Male")), time = factor(c("Lunch","Dinner","Lunch","Dinner"), levels=c("Lunch","Dinner")), total_bill = c(13.53, 16.81, 16.24, 17.42))

p <- ggplot(data=dat1, aes(x=time, y=total_bill, fill=sex)) + geom_bar(colour="black", stat="identity", position=position_dodge(), size=.3) + xlab("Time of day") + ylab("Total bill") + ggtitle("Average bill for 2 people") + theme_bw()

p <- ggplotly(p)

periscope.plotly(p)

# expect-plotly
# expect-output-to-have: Average bill for 2 people
