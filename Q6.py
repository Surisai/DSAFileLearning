# height method for binary Tree


def height(self):
    def helper(node):
        if node is None;
            return -1
        return 1+ max(helper(node.left), helper(node.right))
    return helper(self.root)