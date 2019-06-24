# taken from https://media.readthedocs.org/pdf/lifelines/latest/lifelines.pdf
from lifelines.datasets import load_waltons
df = load_waltons() # returns a Pandas DataFrame

print(df.head())

# expect-output-to-have: 0   6.0  1  miR-137
