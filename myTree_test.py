from myTree import myTree

'''
root_node = myTree("colour")
root_node.add_children(["bitterness", "alcohol"])

first_left_child = myTree(root_node.children[0][0])
first_right_child = myTree(root_node.children[0][1])
first_left_child.add_children(["stout", "larger"])

second_left_child = myTree(root_node.children[0][0])
second_right_child = myTree(root_node.children[0][1])

#print(first_left_child.children)
#print()'''

tree1 = myTree("calorific_value")
tree1.add_left_child("stout")
tree1.add_right_child("lager")

tree2 = myTree("colour")
tree2.add_left_child("ale")
tree2.add_right_child("lager")

tree3 = myTree("bitterness")
tree3.add_left_child(tree1)
tree3.add_right_child(tree2)

tree4 = myTree("alcohol")
tree4.add_left_child("lager")
tree4.add_right_child(tree3)

tree5 = myTree("bitterness")
tree5.add_left_child("stout")
tree5.add_right_child("lager")

tree6 = myTree("colour")
tree6.add_left_child(tree5)
tree6.add_right_child(tree4)

column_headings = ["calorific_value", "nitrogen", "turbidity", "alcohol", "sugars", "bitterness", "beer_id", "colour", "degree_of_fermentation"]
prediction = tree6.traverse([41.72123894, 0.503275756, 2.628181818 ,4.015384615, 16.73, 10.45278947, 93, 13.44,	55.33714286])
print(prediction)


