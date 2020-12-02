from myDecisionTreeClassifier import MyDecisionTreeClassifier

# initialise classifier
classifier = MyDecisionTreeClassifier()

X_test = ["ale", "ale", "stout"]
y_test = ["ale", "stout", "stout"]

# Count results
results = classifier.score(X_test, y_test)
print(results)