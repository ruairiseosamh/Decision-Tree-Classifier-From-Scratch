import pandas as pd
import numpy as np
import collections

class MyDecisionTreeClassifier():
    def __init__(self):
        pass

    def fit(self, X_train, y_train):
        for _ in range(len(X_train)):
            print("hi")

    def predict(self, X_test):
        predictions = []
        return predictions

    def score(self, X_test, y_test):
        score = 0
        for i in range(len(X_test)):
            if(X_test[i] == y_test[i]):
                score = score + 1
        return score

    def get_entropy(self, X, y):
        # Get probability
        probablities = dict()
        frequencies = collections.Counter(y.values.flatten())
        for key in frequencies:
            frequencies[key] /= len(y)
        print(frequencies)

    #def get_targets(self, y):
        #print(np.unique(y)) 