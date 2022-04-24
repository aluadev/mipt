import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
import random

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

random_state = 42
train_size = 0.75
class Builder:
    def __init__(self, X_train: np.ndarray, y_train: np.ndarray):
        self.X_train = X_train
        self.y_train = y_train

    def get_subsample(self, df: int):
        X = self.X_train.copy()
        y = self.y_train.copy()
        X, y = shuffle(X, y, random_state=random_state)
        n_rand = random.randrange(10, len(y))
        return X[:n_rand, :], y[:n_rand]

if __name__ == "__main__":
    X, y = load_iris(return_X_y=True)
    X, y = shuffle(X, y, random_state=random_state)
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_size, random_state=random_state)
    clf = DecisionTreeClassifier(random_state=random_state)
    pattern_item = Builder(X_train, y_train)
    for d in range(10, 100, 10):
        curr_X_train, curr_y_train = pattern_item.get_subsample(d)
        clf.fit(curr_X_train, curr_y_train)
        y_test_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_test_pred)
        print(f"d = {d}%, accuracy on test = {accuracy}")