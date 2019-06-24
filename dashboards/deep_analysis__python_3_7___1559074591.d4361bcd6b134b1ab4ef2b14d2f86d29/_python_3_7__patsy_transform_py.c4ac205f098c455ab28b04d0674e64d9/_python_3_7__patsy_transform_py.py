from patsy import dmatrix
x = [1,2,3,4,5]
# Make sure we can use stateful transforms inside of data matrices
y = dmatrix("bs(x, df=6, degree=3, include_intercept=True) - 1", {"x": x})

print(y[1][0])

# expect-output-to-have: 0.01562499999999997
