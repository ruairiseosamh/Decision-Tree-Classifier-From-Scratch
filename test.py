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
y = pd.DataFrame(df,columns=["style"])

# split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)#, random_state=0)

# initialise classifier
# classifier = DecisionTreeClassifier()
classifier = MyDecisionTreeClassifier()

# Fit classifier
classifier.fit(X_train, y_train)

# Make predictions
predictions = classifier.predict(X_test)
#print(predictions)

# Count results
#results = classifier.score(X_test, y_test)
results = classifier.score(predictions, y_test)
print(str(results/len(predictions) * 100) + "%")
# print(y.head())
predictions_df = pd.DataFrame(predictions)

# Output results to a file
#y_test.to_excel("output1.xlsx")
#predictions_df.to_excel("output2.xlsx")
