class myTree:
    def __init__(self, root, left_child, right_child, threshold):#  nodes):
        #self.nodes = nodes 
        self.root = root
        #self.root = None
        #self.nodes = None
        self.right_child = right_child
        self.left_child = left_child
        self.threshold = threshold
        #self.iteration = 0 

    def add_left_child(self, child):#, left_threshold):
        self.left_child = child
        #self.left_threshold = left_threshold

    def add_right_child(self, child):# ,right_threshold):
        self.right_child = child
        #self.right_threshold = right_threshold

    def traverse(self, value):#, thresholds):
     
        if(value[1][self.root] <= self.threshold):
            if(type(self.left_child) != str):
                return(self.left_child.traverse(value))
            else:
                answer = self.left_child 
                return(answer)
        else:
            if(type(self.right_child) != str):
                return(self.right_child.traverse(value))
            else:
                answer = self.right_child
                return(answer)


    