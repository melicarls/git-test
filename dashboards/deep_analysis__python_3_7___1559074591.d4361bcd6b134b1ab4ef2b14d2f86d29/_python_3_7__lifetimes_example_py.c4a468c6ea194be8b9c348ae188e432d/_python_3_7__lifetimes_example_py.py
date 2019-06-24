# Example 1
from lifetimes.datasets import load_cdnow_summary
data = load_cdnow_summary(index_col=[0])

# Example 2
from lifetimes import BetaGeoFitter

# similar API to scikit-learn and lifelines.
bgf = BetaGeoFitter(penalizer_coef=0.0)
bgf.fit(data['frequency'], data['recency'], data['T'])

from lifetimes.plotting import plot_frequency_recency_matrix

periscope.output(plot_frequency_recency_matrix(bgf))

# expect-image
