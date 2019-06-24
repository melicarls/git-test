from sklearn import datasets
from sklearn.cross_validation import train_test_split

iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


import xgboost as xgb

dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)
param = {'max_depth': 3, 'eta': 0.3, 'silent': 1, 'objective': 'multi:softprob', 'num_class': 3}
num_round = 20  # the number of training iterations

bst = xgb.train(param, dtrain, num_round)
print(type(bst.get_score()))

# expect-output-to-have: dict
