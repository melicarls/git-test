library(plyr)
library(reshape2)
library(plotly)

set.seed(1234)
x<- rnorm(100)
y.1<-rnorm(100)
y.2<-rnorm(100)
y.3<-rnorm(100)
y.4<-rnorm(100)

df<- (as.data.frame(cbind(x,y.1,y.2,y.3,y.4)))

dfmelt<-melt(df, measure.vars = 2:5)

p <- ggplot(dfmelt, aes(x=factor(round_any(x,0.5)), y=value,fill=variable)) + geom_boxplot() + facet_grid(.~variable) + labs(x="X (binned)") + theme(axis.text.x=element_text(angle=-90, vjust=0.4,hjust=1))

p <- ggplotly(p)

# Output to UI
periscope.plotly(p)

# expect-plotly
# expect-output-to-have: X (binned)
