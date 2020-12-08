# import relevant modules
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from myDecisionTreeClassifier import MyDecisionTreeClassifier

# read in dataset
column_headings = ["calorific_value", "nitrogen", "turbidity", "style", "alcohol", "sugars", "bitterness", "beer_id", "colour", "degree_of_fermentation"]
df = pd.read_csv('beer.txt', sep = '\t', header=None,names=column_headings)

# split dataset into inputs and outputs
X = pd.DataFrame(df,columns=["calorific_value", "nitrogen", "turbidity", "alcohol", "sugars", "bitterness", "beer_id", "colour", "degree_of_fermentation"])

'''
for i in X.iterrows():
        #for x in np.arange(sorted.head(1)[column_heading].values, sorted.tail(1)[column_heading].values, 0.1):
    i[1].colour = 1

for i in X.iterrows():
    print(i[1].colour)
    '''

for column_heading in column_headings:
    if(column_heading!="beer_id" and column_heading!="style"):
        max = X[column_heading].max()
        min = X[column_heading].min()
        X[column_heading] = ((X[column_heading] - min) / (max - min))

print(X.head(5))