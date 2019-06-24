# Based on https://cran.r-project.org/web/packages/ltm/ltm.pdf

library(ltm)

## LRT between the constrained and unconstrained GRMs
## for the Science data:
fit0 <- grm(Science[c(1,3,4,7)], constrained = TRUE)
fit1 <- grm(Science[c(1,3,4,7)])
anova(fit0, fit1)
## LRT between the one- and two-factor models
## for the WIRS data:
anova(ltm(WIRS ~ z1), ltm(WIRS ~ z1 + z2))
## An LRT between the Rasch and a constrained
## two-parameter logistic model for the WIRS data:
fit0 <- rasch(WIRS)
fit1 <- ltm(WIRS ~ z1, constraint = cbind(c(1, 3, 5), 2, 1))
anova(fit0, fit1)

## An LRT between the constrained (discrimination
## parameter equals 1) and the unconstrained Rasch
## model for the LSAT data:
fit0 <- rasch(LSAT, constraint = rbind(c(6, 1)))
fit1 <- rasch(LSAT)
anova(fit0, fit1)
## An LRT between the Rasch and the two-parameter
## logistic model for the LSAT data:
anova(rasch(LSAT), ltm(LSAT ~ z1))

# expect-output-to-have: Likelihood Ratio Table
