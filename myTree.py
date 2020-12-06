class myTree:
    def __init__(self, root, left_child, right_child, threshold):#  nodes):
        #self.nodes = nodes 
        self.root = root
        self.root = None
        self.nodes = None
        self.right_child = right_child
        self.left_child = left_child
        self.threshold = None
        self.iteration = 0 

    def add_left_child(self, child):#, left_threshold):
        self.left_child = child
        #self.left_threshold = left_threshold

    def add_right_child(self, child):# ,right_threshold):
        self.right_child = child
        #self.right_threshold = right_threshold

    def traverse(self, value):#, thresholds):
        colour = value[1].colour
        bitterness = value[1].bitterness
        alcohol = value[1].alcohol
        calorific_value = value[1].calorific_value
        thresholds = [9.36, 9.659053, 3.929, 8.174, 41.67, 15.36]

        '''if (self.left_child != None):
            if(colour <= thresholds[0]):
                if(bitterness <= thresholds[1]):
                    return self.left_child.left_child
                else:
                    return self.left_child.right_child
            else:
                if(alcohol <= thresholds[2]):
                    return self.right_child.left_child
                else:
                    if(bitterness <= thresholds[3]):
                        if(calorific_value <= thresholds[4]):
                            return self.right_child.right_child.left_child.left_child
                        else:
                            return self.right_child.right_child.left_child.right_child
                    else:
                        if(colour <= thresholds[5]):
                            return self.right_child.right_child.right_child.left_child
                        else:
                            return self.right_child.right_child.right_child.right_child
        else:
            return self.root'''

        '''if (type(self.left_child) != str):
            if(self.iteration == 1):
                if(colour <= self.threshold):
                    self.left_child.traverse()
                else:
                    self.right_child.traverse()
            #if(self.iteration == 2):
        else:
            # return self.root
            pass'''

        if (self.left_child != None):
            if(colour <= thresholds[0]):
                if(bitterness <= thresholds[1]):
                    return "stout"
                else:
                    return "lager"
            else:
                if(alcohol <= thresholds[2]):
                    return "lager"
                else:
                    if(bitterness <= thresholds[3]):
                        if(calorific_value <= thresholds[4]):
                            return "stout"
                        else:
                            return "lager"
                    else:
                        if(colour <= thresholds[5]):
                            return "ale"
                        else:
                            return "lager"
        #else:
            #return self.root
        
    '''def new_traverse(self, value, thresholds, original, increment):
        if original:
            i = 0
        else:
            i = i+increment

        nodes = ["colour", "bitterness", "alcohol"]
        thresholds = [9.36, 9.659053, 3.929]

        attributes = {}
        for j in len(nodes):
            attributes.add(nodes[j], thresholds[j])
        
        # check if at leaf
        if (self.left_child != None):
            # check if value is less than or equal to threshold
            if(value <= attributes[i][1]):
                new_traverse(self.left_child, value, original=no)
            else:
                new_traverse(self.right_child, value, 2)
        else:
            return self.root'''



    