# import relevant modules
import pandas as pd
import numpy as np
import collections
import math
import operator 


def get_global_entropy(y):
        # Get probability
        entropy = 0
        frequencies = collections.Counter(y.values.flatten())
        for key in frequencies:
            frequencies[key] /= len(y)
            entropy = entropy - (frequencies[key] * math.log2(frequencies[key]))
        
        # print(str(entropy))
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

    #print("less Than = " + str(p_i_less_than))
    #print("Greater Than = " + str(p_i_greater_than))
    #print("Len rows = " + str(len(my_dataset)))

    try:
        #entropy = (-1*p_i_less_than_smaller*math.log2(p_i_less_than_smaller) - (p_i_between*math.log2(p_i_between))- (p_i_greater_than_larger*math.log2(p_i_greater_than_larger)))
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

    #print("entropy = " + str(entropy))
    
    return gain

def get_thresholds(X_train, y_train):
    # read in dataset
    column_headings = ["calorific_value", "nitrogen", "turbidity", "style", "alcohol", "sugars", "bitterness", "beer_id", "colour", "degree_of_fermentation"]
    #df = pd.read_csv('beer.txt', sep = '\t', header=None,names=column_headings)

    #df = pd.merge(X_train, y_train, left_on = 'style')
    X_train['style'] = y_train['style']
    #highest_gain = 0
    #best_targets = []
    styles = []
    gains = []
    lowerThresholds = []
    higherThresholds = []
    outputted_column_headings = []
    highest_overall_gain = 0

    #y = pd.DataFrame(df,columns=["style"])
    global_entropy = get_global_entropy(y_train)
    targets = np.unique(y_train)
        

    # split dataset into attribute and outputs
    # X = pd.DataFrame(df,columns=["colour"])
    for column_heading in column_headings:
        if(column_heading!="beer_id" and column_heading!="style"):
            max = X_train[column_heading].max()
            min = X_train[column_heading].min()

            pairs =  pd.DataFrame(X_train,columns=[column_heading, "style"])
            #pairs =  pd.concat([pd.DataFrame(X_train,columns=[column_heading]), y_train[1]])#, "style"])
            sorted = pairs.sort_values(column_heading, ascending=True)

            for target in targets:
                highest_gain = 0
                best_threshold_x = 0
                best_threshold_z = 0
                styles.append(target)
                outputted_column_headings.append(column_heading)
                

                for x in np.arange(min, max, (max-min)/10):
                    for z in np.arange(min, max, (max-min)/10):
                        #if(x<y):
                        resulting_gain = calculate_gain(sorted, x, z, global_entropy, target, column_heading)
                        if resulting_gain > highest_gain:
                            highest_gain = resulting_gain
                            best_threshold_x = x
                            best_threshold_z = z

                if(highest_gain > highest_overall_gain):
                    highest_overall_gain = highest_gain
                    #highest_overall_gains =  highest_overall_gain + highest_overall_gains 
                    #best_targets = target.append(best_targets)
                #else:
                    #best_targets =  best_targets.append(target)

                gains.append(highest_gain)
                lowerThresholds.append(best_threshold_x)
                higherThresholds.append(best_threshold_z)

                #print("highest information gain for " + target + " in " + column_heading + " achieved is " + str(highest_gain))
                #print("best thresholds are " + str(best_threshold_x) + " " + str(best_threshold_z))

    # print("Best overall gain is " + str(highest_overall_gain))
            #print("Ordered targets are " + best_targets)

    details = zip(outputted_column_headings, gains, styles, lowerThresholds, higherThresholds)

    zipped_details = list(details)

    zipped_details.sort(key = lambda a: a[1], reverse = True)
    #sorted_output = sorted(zipped_details)#, key = gains[1]) # lambda a: a[1])

    #print(zipped_details)
    #print(str(sorted_output))

    return(zipped_details)