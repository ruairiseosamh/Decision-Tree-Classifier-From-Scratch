# Implementation of a Binary Tree which the Decision Tree is based on
class myTree:

    # Initialisation method
    # Can be used to create a tree with or without children or a threshold
    def __init__(self, root, left_child=None, right_child=None, threshold=None):
        # Associate the passed in variables with the instance of the binary tree
        self.root = root
        self.right_child = right_child
        self.left_child = left_child
        self.threshold = threshold

    # Methods to add children to the instance
    def add_left_child(self, child):
        self.left_child = child

    def add_right_child(self, child):
        self.right_child = child


    # Method to recursively traverse the tree
    def traverse(self, value):     
        #  Check to see whether the value being compared against the tree is above or below the relevant threshold 
        if(value[1][self.root] <= self.threshold):
            # If the left child isn't a leaf, recursively call the function with the left child as root
            if(type(self.left_child) != str):
                return(self.left_child.traverse(value))
            else:
                # Otherwise return the leaf
                answer = self.left_child 
                return(answer)
        else:
            # If the right child isn't a leaf, recursively call the function with the right child as root
            if(type(self.right_child) != str):
                return(self.right_child.traverse(value))
            else:
                # Otherwise return the leaf
                answer = self.right_child
                return(answer)


    