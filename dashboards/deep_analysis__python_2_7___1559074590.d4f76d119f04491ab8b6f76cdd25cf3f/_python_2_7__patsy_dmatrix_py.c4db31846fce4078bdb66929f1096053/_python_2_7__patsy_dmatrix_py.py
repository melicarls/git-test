from patsy import dmatrix, demo_data
data = demo_data("a", "b", "x1", "x2", "y", "z column")

# Make sure it is possible to make data matrices
d = dmatrix("x1 + x2", data)

print(d[0][1])

# expect-output-to-have: 1.764052345967664
