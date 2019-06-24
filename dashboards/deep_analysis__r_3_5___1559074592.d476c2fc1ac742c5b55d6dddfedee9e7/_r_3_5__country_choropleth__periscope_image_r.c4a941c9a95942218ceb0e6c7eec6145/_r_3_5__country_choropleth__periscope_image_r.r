library(choroplethr)
data(df_pop_country)

img <- country_choropleth(df_pop_country)
periscope.image(img)

# expect-image
