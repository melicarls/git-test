# Copied from https://seaborn.pydata.org/tutorial/distributions.html

import numpy as np
import seaborn as sns
sns.set(color_codes=True)
np.random.seed(sum(map(ord, "distributions")))
x = np.random.normal(size=100)
periscope.output(sns.distplot(x))

# expect-image