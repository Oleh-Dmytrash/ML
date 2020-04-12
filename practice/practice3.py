import sys
import sklearn.datasets
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X, Y = sklearn.datasets.fetch_california_housing(return_X_y=True)

train_data, test_data, train_result, test_result = train_test_split(X, Y)

skm = LinearRegression()
skm.fit(train_data, train_result)
prediction = skm.predict(test_data)

print(skm.intercept_, skm.coef_)

plt.figure(figsize=(6.8, 5.4))
plt.scatter(test_result, prediction)
plt.plot([0, 5], [0, 7], 'y')
plt.axis('tight')
plt.xlabel('Expected')
plt.ylabel('Predicted')
plt.tight_layout()
plt.show()
