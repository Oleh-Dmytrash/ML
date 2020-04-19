import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

X, y = make_blobs(1000, n_features=2, centers=2, random_state=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=2)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
step = .03

xx, yy = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))

clf = MLPClassifier(hidden_layer_sizes=(50,), max_iter=300, alpha=1e-4,
                    solver='sgd', verbose=10, random_state=1,
                    learning_rate_init=.1
)

clf.fit(X_train, y_train)

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

print("Training set score: %f" % clf.score(X_train, y_train))
print("Test set score: %f" % clf.score(X_test, y_test))

plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=plt.cm.PuOr)

plt.contourf(xx, yy, Z, cmap=plt.cm.PuOr, alpha=0.7)

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.show()