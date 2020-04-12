import sklearn
import numpy as np
from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KneighborsClassifier

dataset = fetch_lfw_people(min_faces_per_person=70, resize=0.4)print(dataset.DESCR)

dataset.data[:5]
dataset.target[:5]
target_names = np.array(dataset.target_names)
target_names[dataset.target[:5]]

X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, random_state=42, test_size=0.25)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
knn.score(X_test, y_test)

param_grid = {
    'n_neighbors': range(1, 5),
    'metric': ["minkowski", "manhattan"]
}
search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5).fit(X_train, y_train)
search
search.best_estimator_.score(X_test, y_test)
