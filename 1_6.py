class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node is not None
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return node

    def _min_value_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def preorder_traversal(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.key)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

def menu():
    tree = BST()
    while True:
        print("\nМеню:")
        print("1. Добавяне на елемент")
        print("2. Търсене на елемент")
        print("3. Изтриване на елемент")
        print("4. Префиксно обхождане")
        print("5. Изход")
        choice = input("Изберете опция: ")
        
        if choice == "1":
            key = int(input("Въведете число: "))
            tree.insert(key)
        elif choice == "2":
            key = int(input("Въведете число за търсене: "))
            print("Намерено" if tree.search(key) else "Не е намерено")
        elif choice == "3":
            key = int(input("Въведете число за изтриване: "))
            tree.delete(key)
        elif choice == "4":
            print("Префиксно обхождане:", tree.preorder_traversal())
        elif choice == "5":
            break
        else:
            print("Невалиден избор!")

if __name__ == "__main__":
    menu()

