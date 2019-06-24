# taken from https://pymc-devs.github.io/pymc/tutorial.html
from pymc.examples import disaster_model
print(disaster_model.switchpoint.parents)

# expect-output-to-have: 'upper': 110
# expect-output-to-have: 'lower': 0
