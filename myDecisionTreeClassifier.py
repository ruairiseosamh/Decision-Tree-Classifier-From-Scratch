import pandas as pd
import numpy as np
import collections
import math

import myTree

class MyDecisionTreeClassifier():
    def __init__(self):
        pass

    def fit(self, X_train, y_train):
        # Build Tree
        '''self.tree.add_left_child("bitterness") 
        self.tree.add_right_child("alcohol")

        first_left_tree = myTree.myTree(self.tree.left_child)
        first_right_tree = myTree.myTree(self.tree.right_child)
        
        first_right_tree.add_right_child("bitterness")
        second_right_tree = myTree.myTree(first_right_tree.right_child)

        second_right_tree.add_left_child("calorific_value")
        second_right_tree.add_right_child("colour")
        third_right_tree = myTree.myTree(second_right_tree.left_child)
        fourth_right_tree = myTree.myTree(second_right_tree.right_child)'''

        self.left_bitterness_tree = myTree.myTree("bitterness", "stout", "lager", 9.659)
        self.calorific_value_tree = myTree.myTree("calorific_value", "stout", "lager", 41.676)
        self.right_colour_tree = myTree.myTree("colour", "ale", "lager", 15.36)
        self.right_bitterness_tree = myTree.myTree("bitterness", self.calorific_value_tree, self.right_colour_tree, 8.17)
        self.alcohol_tree = myTree.myTree("bitterness", "lager", self.right_bitterness_tree, 3.929)
        self.left_colour_tree = myTree.myTree("colour", self.left_bitterness_tree, self.alcohol_tree, 9.36)

    def predict(self, X_test):
        predictions = []

        # Do predictions
        for row in X_test.iterrows():
            prediction = self.left_colour_tree.traverse(row)
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
        # Get probability
        entropy = 0
        frequencies = collections.Counter(y.values.flatten())
        for key in frequencies:
            frequencies[key] /= len(y)
            entropy = entropy - (frequencies[key] * math.log2(frequencies[key]))
        
        print(str(entropy))