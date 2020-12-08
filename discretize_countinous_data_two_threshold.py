# import relevant modules
import pandas as pd
import numpy as np
import collections
import math
import operator 


def get_global_entropy(y):
        entropy = 0
        frequencies = collections.Counter(y.values.flatten())
        for key in frequencies:
            frequencies[key] /= len(y)
            entropy = entropy - (frequencies[key] * math.log2(frequencies[key]))
        
        return entropy

def calculate_gain(my_dataset, my_first_threshold, my_second_threshold, global_entropy, target, column_heading):
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

    below_weighting = p_i_less_than_smaller/len(my_dataset)
    between_weighting = p_i_between/len(my_dataset)
    above_weighting = p_i_greater_than_larger/len(my_dataset)

    gain = global_entropy - (below_weighting * entropy_below) - (between_weighting * entropy_between) - (above_weighting * entropy_above)
    
    return gain

def get_thresholds(X_train, y_train):
    # read in dataset
    column_headings = ["calorific_value", "nitrogen", "turbidity", "style", "alcohol", "sugars", "bitterness", "beer_id", "colour", "degree_of_fermentation"]

    X_train['style'] = y_train['style']
    styles = []
    gains = []
    lowerThresholds = []
    higherThresholds = []
    outputted_column_headings = []
    highest_overall_gain = 0

    global_entropy = get_global_entropy(y_train)
    targets = np.unique(y_train)
        
    # split dataset into attribute and outputs
    for column_heading in column_headings:
        if(column_heading!="beer_id" and column_heading!="style"):
            max = X_train[column_heading].max()
            min = X_train[column_heading].min()

            pairs =  pd.DataFrame(X_train,columns=[column_heading, "style"])
            sorted = pairs.sort_values(column_heading, ascending=True)

            for target in targets:
                highest_gain = 0
                best_threshold_x = 0
                best_threshold_z = 0
                styles.append(target)
                outputted_column_headings.append(column_heading)
                

                for x in np.arange(min, max, (max-min)/10):
                    for z in np.arange(min, max, (max-min)/10):
                        resulting_gain = calculate_gain(sorted, x, z, global_entropy, target, column_heading)
                        if resulting_gain > highest_gain:
                            highest_gain = resulting_gain
                            best_threshold_x = x
                            best_threshold_z = z

                if(highest_gain > highest_overall_gain):
                    highest_overall_gain = highest_gain

                gains.append(highest_gain)
                lowerThresholds.append(best_threshold_x)
                higherThresholds.append(best_threshold_z)

    details = zip(outputted_column_headings, gains, styles, lowerThresholds, higherThresholds)

    zipped_details = list(details)

    zipped_details.sort(key = lambda a: a[1], reverse = True)

    return(zipped_details)