# Example taken from http://dfm.io/emcee/current/user/quickstart/

import numpy as np
import emcee
import matplotlib.pyplot as plt

def lnprob(x, mu, icov):
  diff = x-mu
  return -np.dot(diff,np.dot(icov,diff))/2.0

ndim = 50

means = np.random.rand(ndim)

cov = 0.5 - np.random.rand(ndim ** 2).reshape((ndim, ndim))
cov = np.triu(cov)
cov += cov.T - np.diag(cov.diagonal())
cov = np.dot(cov,cov)

icov = np.linalg.inv(cov)

nwalkers = 250
p0 = np.random.rand(ndim * nwalkers).reshape((nwalkers, ndim))
sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=[means, icov])
lnprob(p0[0], means, icov)
pos, prob, state = sampler.run_mcmc(p0, 100)
sampler.reset()

sampler.run_mcmc(pos, 1000)

for i in range(ndim):
  plt.figure()
  plt.hist(sampler.flatchain[:,i], 100, color="k", histtype="step")
  plt.title("Dimension {0:d}".format(i))

periscope.output(plt)

# expect-image