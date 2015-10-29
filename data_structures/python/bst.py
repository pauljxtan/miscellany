class BST(object):
    """
    A binary search tree. Just a simple wrapper class, which isn't strictly
    necessary as we could represent a tree simply in terms of its root node.
    (But this seems neater.)
    """
    def __init__(self, value=None):
        self.root = BSTNode(value)

    def insert(self, value):
        self.root.insert(value)

    # TODO: decorators?
    def traverse_preorder(self, visit_func):
        if self.root.value:
            self.root.traverse_preorder(visit_func)

    def traverse_inorder(self, visit_func):
        if self.root.value:
            self.root.traverse_inorder(visit_func)

    def traverse_postorder(self, visit_func):
        if self.root.value:
            self.root.traverse_postorder(visit_func)

    def is_empty(self):
        return self.root.value is None

    def get_height(self):
        return

    def get_size(self):
        return

class BSTNode(object):
    """
    A node in a binary search tree.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BSTNode(value)
            elif value > self.value:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)
            else:
                raise ValueError("Value (%d) already exists" % value)
        else:
            self.value = value

    def traverse_preorder(self, visit_func):
        if self.value:
            visit_func(self)
        if self.left:
            self.left.traverse_preorder(visit_func)
        if self.right:
            self.right.traverse_preorder(visit_func)

    def traverse_inorder(self, visit_func):
        if self.left:
            self.left.traverse_inorder(visit_func)
        if self.value:
            visit_func(self)
        if self.right:
            self.right.traverse_inorder(visit_func)
    
    def traverse_postorder(self, visit_func):
        if self.left:
            self.left.traverse_postorder(visit_func)
        if self.right:
            self.right.traverse_postorder(visit_func)
        if self.value:
            visit_func(self)

if __name__ == '__main__':
    import random

    def print_node_value(node):
        print node.value

    values = list(range(1, 11))
    random.shuffle(values)
    print values

    tree = BST()
    print tree.is_empty()
    for value in values:
        tree.insert(value)
    print tree.is_empty()

    print
    tree.traverse_preorder(print_node_value)
    print
    tree.traverse_inorder(print_node_value)
    print
    tree.traverse_postorder(print_node_value)
