# import relevant modules 
import pandas as pd
import numpy as np
import collections
import math

# import relevant project files
import myTree
import discretize_countinous_data_two_threshold

# Implementation of the Decision Tree Classifier
class MyDecisionTreeClassifier():

    # Initialisation method
    def __init__(self):
        pass


    # Method to build the decision tree
    def fit(self, X_train, y_train):
        # Get an list of values ordered on informaiton gain which tell you about the most effective attributes to build the tree on 
        tree_values = discretize_countinous_data_two_threshold.get_thresholds(X_train, y_train)
        
        # Build Tree
        # The two most common trees are either one with a root based on colour or nitrogen
        if(tree_values[0][0]=="colour"):
            # For the colour based tree, build the structure with a nested tree who's root is the second most valable attribute
            self.tree = myTree.myTree(tree_values[0][0],tree_values[0][2],myTree.myTree(tree_values[1][0],"lager","ale",tree_values[1][4]),tree_values[0][4])
        elif(tree_values[0][0]=="nitrogen"):
            # For the nitrogen based tree, build the structure with a nested tree who's root is the second most valable attribute
            self.tree = myTree.myTree(tree_values[0][0],myTree.myTree(tree_values[1][0],tree_values[1][2],"lager",tree_values[1][3]),"ale",tree_values[0][4])
        else:
            # Very rarely does a different type of tree occour but this is handled here
            print("Unusual tree configuration found. Please retry")
    

    # Prediction method
    def predict(self, X_test):
        # Initialise an array to store the predictions
        predictions = []

        # Loop through each row in the test data and make a prediction based on the decision tree traversal
        for row in X_test.iterrows():
            prediction = self.tree.traverse(row)
            predictions.append(prediction)
        return predictions


    # Scoring method
    def score(self, X_test, y_test):
        # Initialise variables
        score = 0
        j = 0

        # Loop through each prediciton and actual y value and count how many times the algorithm got it right
        for i in y_test.iterrows():
            if(X_test[j] == i[1]['style']):
                score = score + 1
            j = j + 1
        return score