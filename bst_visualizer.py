import time

class Node:
    """
    Binary Search Tree Node representation.
    Each node holds a value and references to its left and right children.
    """
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BSTAnalyzer:
    def __init__(self):
        self.root = None
        self.steps = []

    def insert(self, key):
        """Inserts a key and logs the path taken for analysis."""
        path = []
        if self.root is None:
            self.root = Node(key)
            self.steps.append(f"Element {key}: Set as Root.")
        else:
            self._insert_recursive(self.root, key, path)
            step_desc = f"Element {key}: Path taken -> {' -> '.join(path)}."
            self.steps.append(step_desc)

    def _insert_recursive(self, current, key, path):
        path.append(str(current.val))
        if key < current.val:
            if current.left is None:
                current.left = Node(key)
                path.append(f"Placed Left of {current.val}")
            else:
                self._insert_recursive(current.left, key, path)
        else:
            if current.right is None:
                current.right = Node(key)
                path.append(f"Placed Right of {current.val}")
            else:
                self._insert_recursive(current.right, key, path)

    def display_structure(self, node, level=0, prefix="Root: "):
        """Visualizes the tree structure in a top-down format."""
        if node is not None:
            print(" " * (level * 6) + prefix + f"[{node.val}]")
            if node.left or node.right:
                if node.left:
                    self.display_structure(node.left, level + 1, "L── ")
                else:
                    print(" " * ((level + 1) * 6) + "L── [None]")
                
                if node.right:
                    self.display_structure(node.right, level + 1, "R── ")
                else:
                    print(" " * ((level + 1) * 6) + "R── [None]")

def run_simulation():
    dataset = [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]
    analyzer = BSTAnalyzer()
    
    print("="*50)
    print("ROWEZ ELITE BST ANALYZER v2.0")
    print("="*50)
    print(f"Target Dataset: {dataset}\n")

    for val in dataset:
        analyzer.insert(val)
        print(f"[LOG] {analyzer.steps[-1]}")
        time.sleep(0.1)  # Simulation delay

    print("\n" + "="*50)
    print("FINAL BST ARCHITECTURE")
    print("="*50)
    analyzer.display_structure(analyzer.root)
    print("="*50)
    
    print("\n[ALGORITHM ANALYSIS]")
    print(f"- Node Count: {len(dataset)}")
    print("- Best Case Complexity: O(log n)")
    print("- Worst Case Complexity: O(n) - (If data was sorted)")
    print("- Traversal Method: Depth-First Search Logic")

if __name__ == "__main__":
    run_simulation()
