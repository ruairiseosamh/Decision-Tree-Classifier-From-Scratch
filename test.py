# import relevant modules
import pandas as pd
import sys
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from myDecisionTreeClassifier import MyDecisionTreeClassifier

def main(filename):
    # read in dataset
    column_headings = ["calorific_value", "nitrogen", "turbidity", "style", "alcohol", "sugars", "bitterness", "beer_id", "colour", "degree_of_fermentation"]
    df = pd.read_csv(filename, sep = '\t', header=None,names=column_headings)

    # split dataset into inputs and outputs
    X = pd.DataFrame(df,columns=["calorific_value", "nitrogen", "turbidity", "alcohol", "sugars", "bitterness", "beer_id", "colour", "degree_of_fermentation"])
    y = pd.DataFrame(df,columns=["style"])

    # split the dataset into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

    # initialise classifier
    built_in_classifier = DecisionTreeClassifier()
    classifier = MyDecisionTreeClassifier()

    # Fit classifier
    built_in_classifier.fit(X_train, y_train)
    classifier.fit(X_train, y_train)
    
    # Make predictions
    built_in_predictions = built_in_classifier.predict(X_test)
    predictions = classifier.predict(X_test)

    # Count results
    built_in_results = built_in_classifier.score(X_test, y_test)
    results = classifier.score(predictions, y_test)

    # Convert Scores to Percentages
    built_in_accuracy=(built_in_results* 100)
    accuracy = (results/len(predictions) * 100)

    # Convert prediction arrays to pandas dataframes for export
    built_in_predictions_df = pd.DataFrame(built_in_predictions)
    predictions_df = pd.DataFrame(predictions)

    # Output results to csv files
    y_test.to_csv("Actual_answers.csv")
    predictions_df.to_csv("My_Classifier_Predictions.csv")
    built_in_predictions_df.to_csv("Built_in_Classifier_Predictions.csv")

    # Write accuracies to a text file
    with open("accuracies.txt", "w") as file:
        file.write("Built in classifier accuracy: " + str(built_in_accuracy) + "%\n")
        file.write("My classifier accuracy: " + str(accuracy) + "%\n")

if __name__ == "__main__":
    main(sys.argv[1])