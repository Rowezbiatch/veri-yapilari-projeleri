class Node:
    """BST Düğüm Yapısı"""
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    """BST'ye yeni eleman ekleme fonksiyonu"""
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def print_tree(node, level=0, prefix="Root: "):
    """Ağaç yapısını terminalde görselleştirme"""
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

# Kullanıcıdan gelen dizi
data = [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]

# BST Oluşturma
root = None
for item in data:
    root = insert(root, item)

# Sonucu Yazdır
print("--- Rowez BST Structure ---")
print_tree(root)