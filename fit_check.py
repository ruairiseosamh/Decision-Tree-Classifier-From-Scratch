# import relevant modules
import pandas as pd
import numpy as np
from myDecisionTreeClassifier import MyDecisionTreeClassifier

# read in dataset
column_headings = ["calorific_value", "nitrogen", "turbidity", "style", "alcohol", "sugars", "bitterness", "beer_id", "colour", "degree_of_fermentation"]
df = pd.read_csv('beer.txt', sep = '\t', header=None,names=column_headings)

# split dataset into inputs and outputs
X = pd.DataFrame(df,columns=["calorific_value", "nitrogen", "turbidity", "alcohol", "sugars", "bitterness", "beer_id", "colour", "degree_of_fermentation"])
y = pd.DataFrame(df,columns=["style"])

classifier = MyDecisionTreeClassifier()

classifier.fit(X, y)