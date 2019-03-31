#!/bin/python3


class Node:
    '''Classe que representa um No da Árvore binária'''

    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.right = right
        self.left = left
        self.parent = parent


class Tree:
    '''Classe que representa uma Árvore Binária'''

    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root is None

    def insert_node(self, node=None):
        # se value for None já descartamos
        if (node is None):
            return
        else:
            root = self.root
            last_node = None
            while (root is not None):
                last_node = root
                if (node.data < root.data):
                    root = root.left
                else:
                    root = root.right

            node.parent = last_node
            if (last_node is None):
                self.root = node
            else:
                if (node.data < last_node.data):
                    last_node.left = node
                else:
                    last_node.right = node

    def find_node(self, value=None):
        if (value is None):
            return
        if (self.is_empty()):
            return
        else:
            root = self.root
            while (root is not None):
                if (root.data == value):
                    return root
                if (value < root.data):
                    root = root.left
                else:
                    root = root.right
            return None

    def __find_node_recursively(self, node, value):
        if (node is None or node.data == value):
            return node
        if (node.data > value):
            return self.__find_node_recursively(node.right, value)
        else:
            return self.__find_node_recursively(node.left, value)

    def find_node_recursively(self, value=None):
        if (value is None):
            return
        if (self.is_empty()):
            return
        root = self.root
        return self.__find_node_recursively(root, value)

    def get_min_node(self, node=None):
        if (self.is_empty()):
            return

        if (node is None):
            node = self.root

        while (node.left is not None):
            node = node.left

        return node

    def get_max_node(self, node=None):
        if (self.is_empty()):
            return

        if (node is None):
            node = self.root

        while (node.right is not None):
            node = node.right

        return node

    def __pre_order(self, node):
        if (node is None):
            return
        print(node.data, end=' ')
        self.__pre_order(node.left)
        self.__pre_order(node.right)

    def pre_order(self):
        if (self.is_empty()):
            return
        root = self.root
        self.__pre_order(root)

    def __pos_order(self, node):
        if (node is None):
            return
        self.__pos_order(node.left)
        self.__pos_order(node.right)
        print(node.data, end=' ')

    def pos_order(self):
        if (self.is_empty()):
            return
        root = self.root
        self.__pos_order(root)

    def __in_order(self, node):
        if (node is None):
            return
        self.__in_order(node.left)
        print(node.data, end=' ')
        self.__in_order(node.right)

    def in_order(self):
        if (self.is_empty()):
            return
        root = self.root
        self.__in_order(root)

    def __check_bst(self, node, min, max):
        if (node is None):
            return True

        if (node.data < min or node.data > max):
            return False

        return (self.__check_bst(node.left, min, node.data-1) and self.__check_bst(node.right, node.data+1, max))

    def is_bst(self):
        if (self.is_empty()):
            return
        root = self.root
        min_left = self.get_min_node(root)
        max_left = self.get_max_node(root)
        return self.__check_bst(root, min_left.data, max_left.data)

    def __height(self, node):
        if (node is None):
            return -1

        height_left = self.__height(node.left)
        height_right = self.__height(node.right)
        if (height_left > height_right):
            return (height_left + 1)
        else:
            return (height_right + 1)

    def get_height(self):
        if (self.is_empty()):
            return
        root = self.root
        return self.__height(root)

    def __change_nodes(self, node, node_leaf):
        if (node.parent is None):
            self.root = node_leaf
        elif (node == node.parent.left):
            node.parent.left = node_leaf
        else:
            node.parent.right = node_leaf
        if (node_leaf is not None):
            node_leaf.parent = node.parent


    def __delete_node(self, node):
        if (node.left is None):
            self.__change_nodes(node, node.right)
        elif (node.right is None):
            self.__change_nodes(node, node.left)
        else:
            y = self.get_min_node(node.right)
            if y.parent != node:
                self.__change_nodes(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.__change_nodes(node, y)
            y.left = node.left
            y.left.parent = y

    def remove(self, value=None):
        if (value is None):
            return
        if (self.is_empty()):
            return
        else:
            #procura pelo nó
            node = self.find_node(value)
            # nó não encontrado
            if (node is None):
                return
            self.__delete_node(node)
            


if __name__ == "__main__":
    Tree = Tree()
    # node = Tree.find_node_recursively(20)
    Tree.insert_node(Node(50))
    Tree.insert_node(Node(30))
    Tree.insert_node(Node(20))
    Tree.insert_node(Node(40))
    Tree.insert_node(Node(35))
    Tree.insert_node(Node(37))
    Tree.insert_node(Node(45))
    Tree.insert_node(Node(100))
    node = Tree.find_node(10)
    node = Tree.find_node_recursively(10)
    Tree.pre_order()
    print()
    Tree.pos_order()
    print()
    Tree.in_order()
    print()
    print(Tree.is_bst())
    print()
    print(Tree.get_height())
    print()
    Tree.remove(35)
    print()
    Tree.in_order()
