# **Exam Review Answers**

# **1. Why is search() in a balanced BST O(log n)?**
# A balanced BST divides the data almost evenly at each level. With each comparison, the search space is halved, similar to binary search. This results in logarithmic time complexity: O(log n).

# **2. Why use a max\_heap for ascending order heap sort?**
# A max\_heap ensures the largest element is at the root. During heap sort, the root (max value) is swapped to the end of the array. The heap is restructured and repeated, placing elements in ascending order from the back.

# **3. Best data structure for reverse phone directory?**
# A hash table (dictionary/map) is ideal, using phone numbers as keys and names as values. This allows O(1) average lookup time.

# **4. Can you binary search a sorted linked list?**
# Not efficiently. Binary search needs direct access to the middle element, but linked lists require traversal from the head, resulting in O(n) time instead of O(log n).

# **5. BST: print\_between(min, max)**

# ```python
    def print_between(self, min, max):
        def _print_between(node):
            if not node:
                return
            if node.value > min:
                _print_between(node.left)
            if min <= node.value <= max:
                print(node.value)
            if node.value < max:
                _print_between(node.right)
        _print_between(self.root)
# ```
def print_between_descending(self, min_val, max_val):
    def helper(node):
        if node is None:
            return
        if node.value < min_val:
            helper(node.right)
        elif node.value > max_val:
            helper(node.left)
        else:
            # Traverse right first to get larger values first
            helper(node.right)
            print(node.value)
            helper(node.left)
    helper(self.root)
#########Example full code
    class BST:
    class Node:
        def __init__(self, value=None, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    # Insert helper to build the BST for testing
    def insert(self, value):
        def _insert(node, value):
            if node is None:
                return self.Node(value)
            elif value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        self.root = _insert(self.root, value)

    # Method to print values between min and max in descending order
    def print_between_descending(self, min_val, max_val):
        def helper(node):
            if node is None:
                return
            if node.value < min_val:
                helper(node.right)
            elif node.value > max_val:
                helper(node.left)
            else:
                helper(node.right)
                print(node.value)
                helper(node.left)
        helper(self.root)

# ---------- TEST CODE BELOW ----------

# Create BST and insert values
tree = BST()
values_to_insert = [50, 30, 70, 20, 40, 60, 80, 35, 45, 65, 75]
for val in values_to_insert:
    tree.insert(val)

# Print values between 35 and 70 in descending order
print("Values between 35 and 70 (descending):")
tree.print_between_descending(35, 70)
#--------Test 
class BST:
    class Node:
        def __init__(self, value=None, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    # Insert helper to build the BST for testing
    def insert(self, value):
        def _insert(node, value):
            if node is None:
                return self.Node(value)
            elif value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        self.root = _insert(self.root, value)

    # Descending order: Right → Node → Left
    def print_between_descending(self, min_val, max_val):
        def helper(node):
            if node is None:
                return
            if node.value < min_val:
                helper(node.right)
            elif node.value > max_val:
                helper(node.left)
            else:
                helper(node.right)
                print(node.value)
                helper(node.left)
        helper(self.root)

    # Ascending order: Left → Node → Right
    def print_between_ascending(self, min_val, max_val):
        def helper(node):
            if node is None:
                return
            if node.value > min_val:
                helper(node.left)
            if min_val <= node.value <= max_val:
                print(node.value)
            if node.value < max_val:
                helper(node.right)
        helper(self.root)

# ---------- TEST CODE ----------

# Create BST and insert values
tree = BST()
values_to_insert = [50, 30, 70, 20, 40, 60, 80, 35, 45, 65, 75]
for val in values_to_insert:
    tree.insert(val)

# Test ascending
print("Values between 35 and 70 (ascending):")
tree.print_between_ascending(35, 70)

# Test descending
print("\nValues between 35 and 70 (descending):")
tree.print_between_descending(35, 70)

# **6. BT: height()**

# ```python
    def height(self):
        def _height(node):
            if not node:
                return -1
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)
# ```
#---- full code
class BT:
    class Node:
        def __init__(self, value=None, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    # Insert helper to build a binary tree manually (not BST logic)
    def insert_level_order(self, values):
        """Insert nodes into the binary tree in level-order (left to right)."""
        from collections import deque
        if not values:
            return

        self.root = self.Node(values[0])
        queue = deque([self.root])
        i = 1

        while i < len(values):
            current = queue.popleft()
            if values[i] is not None:
                current.left = self.Node(values[i])
                queue.append(current.left)
            i += 1

            if i < len(values) and values[i] is not None:
                current.right = self.Node(values[i])
                queue.append(current.right)
            i += 1

    # Height of the binary tree
    def height(self):
        def helper(node):
            if node is None:
                return -1  # height of an empty tree is -1
            left_height = helper(node.left)
            right_height = helper(node.right)
            return 1 + max(left_height, right_height)

        return helper(self.root)
## low case
# Inside the BT class
def min_depth(self):
    def helper(node):
        if node is None:
            return 0
        # If one of the children is None, ignore it in min comparison
        if node.left is None and node.right is not None:
            return 1 + helper(node.right)
        if node.right is None and node.left is not None:
            return 1 + helper(node.left)
        return 1 + min(helper(node.left), helper(node.right))
    return helper(self.root)
#Test
# Same tree as before
tree = BT()
tree.insert_level_order([10, 20, 30, 40, 50, None, 60, None, None, 70])

# Test max height and min depth
print("Height (max depth):", tree.height())     # Expected: 3
print("Minimum depth:", tree.min_depth())       # Expected: 2 (10 → 30 → 60)

# **7a. Adjacency Matrix and List**
# Let A-B, A-D, B-C, C-E, D-E, E-F, F-G be edges.

# *Adjacency Matrix (A to G rows & cols):*

# ```
#   A B C D E F G
# A 0 1 0 1 0 0 0
# B 0 0 1 0 0 0 0
# C 0 0 0 0 1 0 0
# D 0 0 0 0 1 0 0
# E 0 0 0 0 0 1 0
# F 0 0 0 0 0 0 1
# G 0 0 0 0 0 0 0
# ```

# *Adjacency List:*

# ```
# A: B, D
# B: C
# C: E
# D: E
# E: F
# F: G
# G: -
# ```

# **7b. Dijkstra's Algorithm**
# Assign weights, e.g. A-B(2), A-D(4), B-C(1), C-E(3), D-E(2), E-F(1), F-G(5).
# Use priority queue to find shortest paths from A to all others.

# **8. Binary Tree Tasks (Answer depends on drawn tree)**

# * Leaf nodes: Nodes with no children.
# * Root: The topmost node.
# * Traversals:

#   * Preorder: Root -> Left -> Right
#   * Postorder: Left -> Right -> Root
#   * Inorder: Left -> Root -> Right
#   * Breadthfirst: Level-by-level
# * Height: Longest path from root to a leaf.
# * Depth of leaf: Distance from root to each leaf.

# **9a. BST Insertions**
# Build step by step: insert 80, 70, 60, etc., forming a skewed left tree, but balanced a bit with 35, 45, 43.

# **9b. BST Deletions**
# Remove 10 (leaf), 70 (node with one child), 40 (node with two children). Adjust tree accordingly.

# **10a. Min Heap Insertions**
# Use sift-up after inserting at end. Maintain heap property.

# **10b. Remove root 3 times**
# Each remove() swaps root with last element, deletes last, then heapifies.

# **11. AVL Tree Insertions**
# Add and rebalance after each insert using rotations. Track balance factors.

# **12. Red-Black Tree Insertions**
# Add and rebalance, applying color rules and rotations.

# **13. 2-3 Tree Insertions**
# Maintain nodes with 1 or 2 keys. Split full nodes upward when needed.

# **14a. Binary Tree from List**
# Use level-order insertion to build binary tree from \[15, 12, 14, ..., 1].

# **14b. Min-Heapify**
# Apply heapify from last internal node upward. Final list becomes a valid min-heap.

# **15. BST: inorder\_successor(value)**

# ```python
#     def inorder_successor(self, value):
#         current = self.root
#         successor = None
#         while current:
#             if value < current.value:
#                 successor = current
#                 current = current.left
#             elif value > current.value:
#                 current = current.right
#             else:
#                 if current.right:
#                     temp = current.right
#                     while temp.left:
#                         temp = temp.left
#                     return temp
#                 break
#         return successor
# ```
def inorder_successor(self, value):
    def find(node, value):
        if node is None:
            return None
        if value < node.value:
            return find(node.left, value)
        elif value > node.value:
            return find(node.right, value)
        else:
            return node

    def min_value(node):
        while node.left:
            node = node.left
        return node

    current = self.root
    successor = None
    while current:
        if value < current.value:
            successor = current
            current = current.left
        elif value > current.value:
            current = current.right
        else:
            if current.right:
                return min_value(current.right)
            break
    return successor

# **16. Can you write a program to check for infinite loops?**
# No, in general this is not possible. This is known as the Halting Problem, proven undecidable by Alan Turing. No algorithm can determine for all programs whether they will halt or loop forever.
