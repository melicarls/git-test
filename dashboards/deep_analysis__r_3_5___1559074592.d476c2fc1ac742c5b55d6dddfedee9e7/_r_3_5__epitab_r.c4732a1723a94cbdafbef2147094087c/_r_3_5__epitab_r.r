library(epitools)

data(oswego)
attach(oswego)

epitab(vanilla.ice.cream, ill)

# expect-output-to-have: 0.6206897
