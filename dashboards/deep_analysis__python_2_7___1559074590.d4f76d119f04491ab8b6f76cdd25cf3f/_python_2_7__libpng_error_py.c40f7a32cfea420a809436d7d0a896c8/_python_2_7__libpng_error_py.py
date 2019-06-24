"""
Tests that standard error from shared c libraries are not resulting in 
"Internal Error" messages
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(data=None, columns=['a', 'b'])
f, ax = plt.subplots(len(df.index), figsize=(10, 0))
periscope.image(f)

# expect-output-to-have: RuntimeError
# expect-output-to-have: libpng signaled error
