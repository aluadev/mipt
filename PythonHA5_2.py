import numpy as np
from sklearn.datasets import load_iris
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

random_state = 42
train_size = 0.75


class Module:
    def __init__(self, classifiers) -> None:
        self.classifiers = classifiers
        self.count = len(self.classifiers)

    def fit(self, X, y):
        for classifier in self.classifiers:
            classifier.fit(X, y)

    def predict(self, X):
        y_pred = []
        for classifier in self.classifiers:
            y_pred.append(classifier.predict(X))
        y_pred = np.stack(y_pred)
        return np.floor(y_pred.sum(axis=0) / self.count + 0.5).astype(int)


if __name__ == "__main__":
    X, y = load_iris(return_X_y=True)
    X, y = shuffle(X, y, random_state=random_state)
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_size, random_state=random_state)
    classifiers = [DecisionTreeClassifier(random_state=random_state),
                   RandomForestClassifier(max_depth=5, random_state=random_state),
                   KNeighborsClassifier(5)]

    ensemble = Module(classifiers)
    ensemble.fit(X_train, y_train)
    y_pred = ensemble.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy score achieved with ensemble = {accuracy}")