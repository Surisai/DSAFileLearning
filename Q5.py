# question 5 print_between method in BST
# this is asending print between the valu

class BST:
    class Node:
        def _init_(self,value=None,)
            

def print_between(self, min_val, max_val):
    def helper(node):
        if node is None:
             return 
        if min_val < node.max_value:
            helper(node.left)
        if min_val <= node.value <= max_val:
            print(node.value)
        if max_val > node.value:
            helper(node.right)
    helper(self.root)


#this is descending print between
def print_between_des(self,min_val,max_val):
    def helper(node):
        if node is None:
            return
        if node.value < max_val:
            helper(node.right)
        if min_val <=node.value <=max_val:
            print(node.vaue)
        if min_val > node.value:
            helper(node.left)
    helper(self.root)