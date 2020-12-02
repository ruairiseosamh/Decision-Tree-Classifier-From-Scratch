class myTree:
    def __init__(self, root):
        self.root = root
        self.right_child = None
        self.left_child = None

    def add_left_child(self, child):
        self.left_child = child

    def add_right_child(self, child):
        self.right_child = child

    def traverse(self, value):
        colour = value[7]
        bitterness = value[6]
        alcohol = value[4]
        calorific_value = value[0]
        if (self.left_child != None):
            if(colour <= 9.36):
                if(bitterness <= 9.659053):
                    return self.left_child.left_child
                else:
                    return self.left_child.right_child
            else:
                if(alcohol <= 3.929):
                    return self.right_child.left_child
                else:
                    if(bitterness <= 8.174):
                        if(calorific_value <= 41.67):
                            return self.right_child.right_child.left_child.left_child
                        else:
                            return self.right_child.right_child.left_child.right_child
                    else:
                        if(colour <= 15.36):
                            return self.right_child.right_child.right_child.left_child
                        else:
                            return self.right_child.right_child.right_child.right_child
        else:
            return self.root



    