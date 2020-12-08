# import relevant modules
import pandas as pd
import numpy as np
import collections
import math
import operator 

# Implementation of helper methods to calculate entrpoty and Information Gain for each attribute as well as their threshold values 

# Method to calculate the global entropy of the targets. This is used in the calculation of Information Gain
def get_global_entropy(y):
        entropy = 0
        frequencies = collections.Counter(y.values.flatten())

        # For each value in the target attribute. Calculate its frequency and from that its entropy
        for key in frequencies:
            frequencies[key] /= len(y)
            entropy = entropy - (frequencies[key] * math.log2(frequencies[key]))

        return entropy


# Method to calculate the Information gain of any given attribute
def calculate_gain(my_dataset, my_first_threshold, my_second_threshold, global_entropy, target, column_heading):
    # Initialise variables
    p_i_less_than_smaller = 0
    p_i_between = 0
    p_i_greater_than_larger = 0
    p_i_less_than_smaller_true = 0
    p_i_between_true = 0
    p_i_greater_than_larger_true = 0
    p_i_less_than_smaller_false = 0
    p_i_between_false = 0
    p_i_greater_than_larger_false = 0
    gain = 0

    # Loop through dataset and count the amount of times an attribute below, between and above a pair of thresholds is corellated correctly and incorrectly
    for _, row in my_dataset.iterrows():
        if(row[column_heading] <= my_first_threshold):
            if(row['style']==target):
                p_i_less_than_smaller_true = p_i_less_than_smaller_true + 1
            else:
                p_i_less_than_smaller_false = p_i_less_than_smaller_false + 1

            p_i_less_than_smaller = p_i_less_than_smaller + 1

        elif(row[column_heading] >= my_first_threshold and row[column_heading] <= my_second_threshold):
            if(row['style']==target):
                p_i_between_true = p_i_between_true + 1
            else:
                p_i_between_false = p_i_between_false + 1
            p_i_between = p_i_between + 1

        else:
            if(row['style']==target):
                p_i_greater_than_larger_true = p_i_greater_than_larger_true + 1
            else:
                p_i_greater_than_larger_false = p_i_greater_than_larger_false + 1
            p_i_greater_than_larger = p_i_greater_than_larger + 1

    # Calculate probabilites in the given ranges
    # Use seperate try except blocks to avoid divide by zero errors
    try:
        p_i_less_than_smaller_true = p_i_less_than_smaller_true/p_i_less_than_smaller
    except:
        p_i_less_than_smaller_true = 0

    try:
        p_i_between_true = p_i_between_true/p_i_between
    except:
        p_i_between_true = 0

    try:
        p_i_greater_than_larger_true = p_i_greater_than_larger_true/p_i_greater_than_larger
    except:
        p_i_greater_than_larger_true = 0
    
    try:
        p_i_less_than_smaller_false = p_i_less_than_smaller_false/p_i_less_than_smaller
    except:
        p_i_less_than_smaller_false = 0

    try:
        p_i_between_false = p_i_between_false/p_i_between
    except:
        p_i_between_false = 0

    try:
        p_i_greater_than_larger_false = p_i_greater_than_larger_false/p_i_greater_than_larger
    except:
        p_i_greater_than_larger_false = 0

    # Calculate entrporys in the given ranges
    # Use seperate try except blocks to avoid log to the base two of zero errors
    try:
        entropy_below = -p_i_less_than_smaller_true * math.log2(p_i_less_than_smaller_true)
    except:
        entropy_below = 0

    try:
        entropy_between = -p_i_between_true * math.log2(p_i_between_true)
    except:
        entropy_between  = 0

    try:
        entropy_above =  -p_i_greater_than_larger_true * math.log2(p_i_greater_than_larger_true)
    except:
        entropy_above = 0

    # Calculate the weighting of each region
    below_weighting = p_i_less_than_smaller/len(my_dataset)
    between_weighting = p_i_between/len(my_dataset)
    above_weighting = p_i_greater_than_larger/len(my_dataset)

    # Calculate gain based on the reduction in global entropy by the individual weighting and entropy multiplications
    gain = global_entropy - (below_weighting * entropy_below) - (between_weighting * entropy_between) - (above_weighting * entropy_above)
    
    return gain


# Method to calculate the most effective threshold values for any given attribute to maximise the information gain from them
def get_thresholds(X_train, y_train):
    # Initialise variables
    column_headings = ["calorific_value", "nitrogen", "turbidity", "style", "alcohol", "sugars", "bitterness", "beer_id", "colour", "degree_of_fermentation"]
    X_train['style'] = y_train['style']
    styles = []
    gains = []
    lowerThresholds = []
    higherThresholds = []
    outputted_column_headings = []

    # Calculate the global entropy
    global_entropy = get_global_entropy(y_train)

    # Get the values of the target variables
    targets = np.unique(y_train)
        
    # Loop through each of the attributes, except beer_id and style as their information gain won't be considered
    for column_heading in column_headings:
        if(column_heading!="beer_id" and column_heading!="style"):

            # Get the range of values in each column to effectively iterate through them with a reasonable resolution size
            max = X_train[column_heading].max()
            min = X_train[column_heading].min()

            # Match each column individually with the target column
            pairs =  pd.DataFrame(X_train,columns=[column_heading, "style"])

            # Sort the dataframe from low to high based on the attribute values
            sorted = pairs.sort_values(column_heading, ascending=True)

            # Loop through each target value, in this case [ale, lager, stout]
            for target in targets:

                # Reset variables to avoid previous values being carried forward through iterations
                highest_gain = 0
                best_threshold_x = 0
                best_threshold_z = 0

                # Keep track of what target is being examined
                styles.append(target)

                # Keep track of what column heading is being examined
                outputted_column_headings.append(column_heading)
                
                # Loop thorugh every possible combination of threshold values in the range in relative increments
                for x in np.arange(min, max, (max-min)/10):
                    for z in np.arange(min, max, (max-min)/10):

                        # Calculate the information gain of each threshold pair on each attribute relative to the target
                        resulting_gain = calculate_gain(sorted, x, z, global_entropy, target, column_heading)

                        # Record the highest gain and at what threshold values it was achieved at
                        if resulting_gain > highest_gain:
                            highest_gain = resulting_gain
                            best_threshold_x = x
                            best_threshold_z = z

                # Keep track of the highest gain achieved for each attribute
                gains.append(highest_gain)

                # Keep track of the threshold values that the highest gains were achieved at
                lowerThresholds.append(best_threshold_x)
                higherThresholds.append(best_threshold_z)

    # Combine the information tracked earlier in the method into one larger data structure
    details = zip(outputted_column_headings, gains, styles, lowerThresholds, higherThresholds)

    # Convert to a list of lists
    zipped_details = list(details)

    # Sort on Information gain from highest to lowest using a lambda function
    zipped_details.sort(key = lambda a: a[1], reverse = True)

    # Return the sorted list of lists
    return(zipped_details)