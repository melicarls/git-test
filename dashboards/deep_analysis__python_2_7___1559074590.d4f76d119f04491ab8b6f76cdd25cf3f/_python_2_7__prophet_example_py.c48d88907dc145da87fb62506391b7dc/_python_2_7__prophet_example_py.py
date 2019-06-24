import six

if six.PY2:
  from StringIO import StringIO
else:
  from io import StringIO

import pandas as pd

TESTDATA = StringIO("""ds;y
2007-12-10;9.59076113897809
2007-12-11;8.51959031601596
""")

df = pd.read_csv(TESTDATA, sep=";")

# Actual test starts here

from fbprophet import Prophet

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=7)

forecast = m.predict(future)

fc = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

periscope.output(fc)

# expect-output-to-have: DS
# expect-output-to-have: YHAT
# expect-output-to-have: YHAT_LOWER
# expect-output-to-have: YHAT_UPPER
