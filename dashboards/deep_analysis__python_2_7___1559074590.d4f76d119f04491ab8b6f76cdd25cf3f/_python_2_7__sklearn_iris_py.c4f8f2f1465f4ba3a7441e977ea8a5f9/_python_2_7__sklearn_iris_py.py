# Copied from http://scikit-learn.org/stable/tutorial/statistical_inference/settings.html

from sklearn import datasets
iris = datasets.load_iris()
data = iris.data
print(data.shape)

# expect-output-to-have: (150, 4)
