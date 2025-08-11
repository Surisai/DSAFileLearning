# Exam Review: Algorithm Analysis and Data Structures
Format:

approx 60% of marks for short/long answers

 approx 40% of marks for coding. (all coding questions are tree related)



Topics:
# Exam Format and Topics

- Approx 60% of marks for short/long answers  
- Approx 40% of marks for coding (all coding questions are tree related)

---

## Topics

- **Algorithm Analysis**

- **Heaps**  
  - What are they  
  - Heap order and completeness  
  - How to insert/remove from heaps  
  - How are they implemented, what is the underlying data structure  
  - How to perform makeheap() in place using heapify()  
  - Heapsort

- **Trees**  
  - Definitions: leaf, root, sibling, height, depth, complete, traversals, branches, etc.

- **Binary Search Tree (BST)**
  - Be able to implement functions for BSTs including both depth-first and breadth-first traversals  
  - Be able to use drawings to show how to perform insertions/removals  
  - Be able to list nodes by all traversal orders (pre-order, post-order, in-order, breadth-first)

- **AVL Trees**  
  - What are they?  
  - Be able to explain what height balanced means  
  - What is the difference between height balanced and perfect balance  
  - How balances are maintained  
  - Be able to use diagrams to explain how AVL trees work (node balance vs relative height of its subtrees)  
  - Be able to use diagrams to show how to perform an insertion including all necessary rotations

- **Red-Black Trees (no coding)**  
  - What are they?  
  - What are the colouring rules and how they affect the tree's height and branch lengths  
  - Be able to use a diagram to show how to perform insertions

- **2-3 Trees (no coding)**  
  - What are they?  
  - Be able to use a diagram to show how to perform insertions

- **Graphs (no coding)**  
  - Vertices, edges, adjacency list, adjacency matrix representation of graphs  
  - Dijkstra's Algorithm, Minimum Spanning Trees

- **Computational Theory**  
  - What is the Halting problem  
  - Decision problem  
  - Undecidable problem

---

## 1. Heaps

### What are they?
- A **heap** is a complete binary tree that satisfies the **heap order property**:
  - **Max-heap:** Parent node ≥ children.
  - **Min-heap:** Parent node ≤ children.

### Heap order and completeness
- **Heap order:** Every parent is larger (max-heap) or smaller (min-heap) than its children.
- **Completeness:** The tree is completely filled except possibly the last level, filled from left to right.

### How to insert/remove from heaps
- **Insert:** Add element at the end, then "sift-up" to restore heap order.
- **Remove (usually root):** Swap root with last element, remove last, then "sift-down" to restore heap order.

### Implementation and underlying data structure
- Usually implemented as an **array**.
- Parent and children indices:
  - Parent of node at `i`: `(i-1)//2`
  - Left child: `2*i + 1`
  - Right child: `2*i + 2`

### MakeHeap() using heapify()
- Start from last non-leaf node and move upwards.
- For each node, "heapify" to fix the heap property.
- Runs in **O(n)** time.

### Heapsort
- Build max heap.
- Swap root with last element, reduce heap size, heapify root.
- Repeat until sorted.

---

## 2. Trees

### Definitions:
- **Leaf:** Node with no children.
- **Root:** Topmost node.
- **Sibling:** Nodes with the same parent.
- **Height:** Length of longest path from node to leaf.
- **Depth:** Length of path from root to node.
- **Complete Tree:** All levels filled except possibly last, filled left to right.
- **Branches:** Paths from root to leaves.
Node: the thing that store the data within the tree . (each circle in the above diagram is a node)

Root Node: the top most node from which all other nodes come from. A is the root node of the tree.

Subtree: Some portion of the entire tree, includes a node (the root of the subtree) and every node that goes downwards from there. A is the root of the entire tree. B is the root of the subtree containing B,D,E and F

Empty trees: A tree with no nodes

Leaf Node: A node with only empty subtrees (no children) Ex. D,E,F,I,J,and G are all leaf nodes

Children: the nodes that is directly 1 link down from a node is that node's child node. Ex. B is the child of A. I is the child of H

Parent the node that is directly 1 link up from a node. Ex. A is parent of B. H is the parent of I

Sibling: All nodes that have the same parent node are siblings Ex. E and F are siblings of D but H is not

Ancestor: All nodes that can be reached by moving only in an upward direction in the tree. Ex. C, A and H are all ancestors of I but G and B are not.

Descendants or Successors of a node are nodes that can be reached by only going down in the tree. Ex. Descendants of C are G,H,I and J

Depth: Distance from root node of tree. Root node is at depth 0. B and C are at depth 1. Nodes at depth 2 are D,E,F,G and H. Nodes at depth 3 are I and J

Height: Total number of nodes from root to furthest leaf. Our tree has a height of 4.

Path: Set of branches taken to connect an ancestor of a node to the node. Usually described by the set of nodes encountered along the path.

Binary tree: A binary tree is a tree where every node has 2 subtrees that are also binary trees. The subtrees may be empty. Each node has a left child and a right child. Our tree is NOT a binary tree because B has 3 children.
### Traversals:
- **Preorder:** Root → Left → Right
- **Inorder:** Left → Root → Right
- **Postorder:** Left → Right → Root
- **Breadth-first:** Level by level

---

## 3. Binary Search Tree (BST)
- HOW is work ???Binary search trees (BST) are binary trees where values are placed in a way that supports efficient searching. In a BST, all values in the left subtree value in current node < all values in the right subtree. This rule must hold for EVERY subtree,
- Can implement:--
- WHY ???? BST --allows us to quickly perform a search on a linking structure (under certain conditions which we will explore later). To find a value, we simply start at the root and look at the value. If our key is less than the value, search left subtree. If key is greater than value search right subtree. It provides a way for us to do a "binary search" on a linked structure which is not possible with a linear linked list. During the search, we will never have to search the subtrees we eliminate in the search process... thus at worst, searching for a value in a binary search tree is equivalent to going through all the nodes from the root to the furthest leaf in the tree.
  - **Insertions** and **Removals** maintaining BST property.
  - **Traversals:** pre-order, in-order, post-order, breadth-first.
  - **Depth-first** and **breadth-first** searches.
  
- Insertions/removals shown by tree diagrams (not coded here).

---

## 4. AVL Trees

### What are they?
- Self-balancing binary search trees.
- Maintains **height balance** where balance factor of each node ∈ {–1, 0, 1}.

### Height balanced vs perfect balance
- **Height balanced:** Height difference of left and right subtrees ≤ 1.
- **Perfectly balanced:** All levels completely filled; stricter than height balance.

### How balances are maintained
- After insertions/removals, perform **rotations** (single or double) to restore balance.

### Insertions with rotations
- If imbalance occurs at node, perform rotations:
  - Left rotation
  - Right rotation
  - Left-Right rotation
  - Right-Left rotation

(Diagrams illustrate subtree heights and rotations.)

---

## 5. Red-Black Trees (No coding)

### What are they?
- Balanced BST with extra color property on nodes (red or black).

### Coloring rules
- Root is black.
- Red nodes cannot have red children (no two reds in a row).
- Every path from root to leaves has the same number of black nodes.
- These rules keep the tree approximately balanced, ensuring operations in **O(log n)**.

### Effect on height and branches
- Height is ≤ 2 × log(n + 1), preventing skewed trees.

### Insertions
- Insert new node as red.
- Fix coloring and rotate as needed to maintain properties.

---

## 6. 2-3 Trees (No coding)

### What are they?
- Balanced search trees where every node has 1 or 2 keys, and 2 or 3 children.
- Nodes split as keys are inserted, keeping tree balanced.

### Insertions
- Insert key, split nodes if full, push middle key up.
- Splits propagate upward as needed.

(Diagrams show node splits and key moves.)

---

## 7. Graphs (No coding)

### Key concepts
- **Vertices:** Nodes.
- **Edges:** Connections between nodes.

### Representations:
- **Adjacency List:** Each vertex stores list of connected vertices.
- **Adjacency Matrix:** 2D matrix indicating edge presence/weight.

### Dijkstra’s Algorithm
- Finds shortest paths from source to all vertices.
- Uses a priority queue to pick closest unvisited node.

### Minimum Spanning Trees (MST)
- Connect all vertices with minimal total edge weight.
- Algorithms: Kruskal’s, Prim’s.

---

## 8. Computational Theory

### Halting Problem
- Deciding if a program halts (terminates) or runs forever.
- Proven **undecidable** by Alan Turing — no general algorithm can solve it for all programs.

### Decision Problem
- Problem with yes/no answer.

### Undecidable Problem
- Problem for which no algorithm can always give correct yes/no answers.

---

# Code Examples for BST Traversals and Functions

```python
# BST: print values between min and max in ascending order
def print_between(self, min_val, max_val):
    def helper(node):
        if not node:
            return
        if node.value > min_val:
            helper(node.left)
        if min_val <= node.value <= max_val:
            print(node.value)
        if node.value < max_val:
            helper(node.right)
    helper(self.root)

# BST: print values between min and max in descending order
def print_between_descending(self, min_val, max_val):
    def helper(node):
        if not node:
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
