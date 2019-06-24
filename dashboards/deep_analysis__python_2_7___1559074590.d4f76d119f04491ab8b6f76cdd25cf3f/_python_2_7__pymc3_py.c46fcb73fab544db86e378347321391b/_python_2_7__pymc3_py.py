import pymc3 as pm
import numpy as np
import scipy.stats as stats

n = 100
heads = 61

a, b = 10, 10
prior = stats.beta(a, b)
post = stats.beta(heads + a, n - heads + b)
ci = post.interval(0.95)

xs = np.linspace(0, 1, 100)

niter = 1000

with pm.Model() as coin_context:
  p = pm.Beta('p', alpha=2, beta=2)
  y = pm.Binomial('y', n=n, p=p, observed=heads)
  trace = pm.sample(niter, progressbar=False, cores=1)

t = trace[niter // 2:]
p = trace.get_values('p', burn=niter // 2, combine=True)

print("Shape")
print(p.shape)

# expect-output-to-have: Shape
# expect-output-to-have: 1000
