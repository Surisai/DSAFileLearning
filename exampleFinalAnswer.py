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

# **6. BT: height()**

# ```python
    def height(self):
        def _height(node):
            if not node:
                return -1
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)
# ```

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

# **16. Can you write a program to check for infinite loops?**
# No, in general this is not possible. This is known as the Halting Problem, proven undecidable by Alan Turing. No algorithm can determine for all programs whether they will halt or loop forever.
