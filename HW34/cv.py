import numpy as np
from sklearn.model_selection import StratifiedKFold
X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
y = np.array([0, 0, 0, 1])
skf = StratifiedKFold(n_splits=2)
aa = skf.get_n_splits(X, y)
print(aa)
print(skf)  
# StratifiedKFold(n_splits=2, random_state=None, shuffle=False)
# for train_index, test_index in skf.split(X, y):
#     print("TRAIN:", train_index, "TEST:", test_index)
#     X_train, X_test = X[train_index], X[test_index]
#     y_train, y_test = y[train_index], y[test_index]
