import pandas as pd
import numpy as np
import collections
import math

import myTree
import discretize_countinous_data_two_threshold

class MyDecisionTreeClassifier():
    def __init__(self):
        pass

    def fit(self, X_train, y_train):
        # Build Tree
        tree_values = discretize_countinous_data_two_threshold.get_thresholds(X_train, y_train)
        if(tree_values[0][0]=="colour"):
            self.tree = myTree.myTree(tree_values[0][0],"stout",myTree.myTree(tree_values[1][0],"lager","ale",tree_values[1][4]),tree_values[0][4])
        elif(tree_values[0][0]=="nitrogen"):
            self.tree = myTree.myTree(tree_values[0][0],myTree.myTree(tree_values[1][0],"stout","lager",tree_values[1][3]),"ale",tree_values[0][4])
        else:
            print("Unusual tree configuration found. Please retry")


    
    def predict(self, X_test):
        predictions = []

        # Do predictions
        for row in X_test.iterrows():
            prediction = self.tree.traverse(row)
            predictions.append(prediction)
            #if(row%15==0):
                #pass
                # Output Progress values to file


        return predictions

    def score(self, X_test, y_test):
        score = 0
        j = 0
        for i in y_test.iterrows():
            if(X_test[j] == i[1]['style']):
                score = score + 1
            j = j + 1
        return score

    def get_global_entropy(self, X, y):
        entropy = 0
        frequencies = collections.Counter(y.values.flatten())
        for key in frequencies:
            frequencies[key] /= len(y)
            entropy = entropy - (frequencies[key] * math.log2(frequencies[key]))
        
        print(str(entropy))