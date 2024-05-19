class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
            self.size += 1
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: Node, value: int) -> None:
        if value == node.value:
            return
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
                self.size += 1
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
                self.size += 1
            else:
                self._insert_recursive(node.right, value)

    def search(self, value: int) -> bool:
        if self.root is None:
            return False
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Node, value: int) -> bool:
        if node is None:
            return False
        elif node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
      
    def in_order_traversal(self, node: Node) -> list[int]:
        result = []
        if node:
            result += self.in_order_traversal(node.left)
            result.append(node.value)
            result += self.in_order_traversal(node.right)
        return result

    def find_min(self) -> int: 
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.value

    def find_max(self) -> int:
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.value

    def height(self) -> int:
        return self._calculate_height(self.root)

    def _calculate_height(self, node: Node) -> int:
        if node is None:
            return 0
        left_height = self._calculate_height(node.left)
        right_height = self._calculate_height(node.right)
        return max(left_height, right_height) + 1

    def count_leaves(self) -> int:
        return self._count_leaves_recursively(self.root)

    def _count_leaves_recursively(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self._count_leaves_recursively(node.left) + self._count_leaves_recursively(node.right)

    def serialize(self) -> str:
        serialized_tree = []
        self._serialize_recursively(self.root, serialized_tree)
        return ",".join(serialized_tree)

    def _serialize_recursively(self, node, serialized_tree):
        if node:
            serialized_tree.append(str(node.value))
            self._serialize_recursively(node.left, serialized_tree)
            self._serialize_recursively(node.right, serialized_tree)

    def deserialize(self, tree: str) -> None:
        if not tree:
            self.root = None
            return
        values = list(map(int, tree.split(",")))
        self.root = self._deserialize_recursively(values)

    def _deserialize_recursively(self, values: list[int]) -> Node:
        if not values:
            return None
        value = values.pop(0)
        node = Node(value)
        
        left_values = []
        right_values = []

        for char in values:
            if char < value:
                left_values.append(char)
            elif char > value:
                right_values.append(char)
                
        node.left = self._deserialize_recursively(left_values)
        node.right = self._deserialize_recursively(right_values)
        return node

def main():
    bst = BST()

    bst.insert(8)
    bst.insert(4)
    bst.insert(2)
    bst.insert(7)
    bst.insert(1)

    print()
    print("*** IN ORDER ***")
    print()
    if bst.root:
        print(bst.in_order_traversal(bst.root))

    print()
    print("*** MINIMUM ***")
    print()
    print(bst.find_min())

    print()
    print("*** MAXIMUM **")
    print()
    print(bst.find_max())

    print()
    print("*** HEIGHT ***")
    print()
    print(bst.height())

    print()
    print("*** TOTAL LEAVES ***")
    print()
    print(bst.count_leaves())

    print()
    print("*** SERIALIZE ***")
    print()
    print(bst.serialize())

    print()
    print("*** DESERIALIZE ***")
    print()
    serialized_tree = "1,8,4,2,7"
    root = bst.deserialize(serialized_tree)
    print(bst.in_order_traversal(root))

if __name__ == "__main__":
    main()
