# Group 43; Tuytte Victor; De Rijck Wout

class RedBlackTreeNode():
    
    def __init__(self, key, value, parent=None, left=None, right=None):
        self._key = key
        self._values = [value]
        self._parent = parent
        self._black = False
        self._left = left
        self._right = right

    def get_key(self):
        return self._key
    
    def get_values(self):
        return self._values

    def add_value(self, value):
        self._values.append(value)

    # Function has been updated to also update the parent   
    def set_right(self, node):
        self._right = node
        node._parent = self

    # Function has been updated to also update the parent    
    def set_left(self, node):
        self._left = node
        node._parent = self
        
    def get_right(self):
        return self._right
    
    def get_left(self):
        return self._left

    # Sets colour of node to black
    def set_black(self):
        self._black = True

    # Set colour of node to red
    def set_red(self):
        self._black = False

    # Checks if node is black
    def is_black(self):
        return self._black

    # Checks if node is red
    def is_red(self):
        return not self._black

class RedBlackTree():
    
    def __init__(self):
        self._root = None
        self._count = 0
        
    def __len__(self):
        return self._count

    def insert(self, key, value):
        # Same insert as binarytree with some edits for BKtree
        if self._root is None:
            self._root = RedBlackTreeNode(key, value)
            # Make sure root is black
            self._root.set_black()
            self._count = 1
        else:
            self._insert(self._root, key, value)

    def _insert(self, node, key, value):
        if node.get_key() == key:
            node.add_value(value)
        else:
            if  key < node.get_key():
                if node.get_left() is None:
                    node.set_left(RedBlackTreeNode(key,value))
                    self._count += 1
                    # Call fixup on added node
                    self.fixup(node.get_left())
                else:
                    self._insert(node.get_left(),key,value)
            else:
                if node.get_right() is None:
                    node.set_right(RedBlackTreeNode(key,value))
                    self._count += 1
                    # Call fixup on added node
                    self.fixup(node.get_right())
                else:
                    self._insert(node.get_right(),key,value)

    def fixup(self, node):
        # Make sure inserted node that needs fixup is red
        node.set_red()
        # Check for not None as None is equivalent with black
        while node._parent is not None and node._parent.is_red():
            # Rename for ease of implementation
            parent = node._parent
            grand_parent = parent._parent

            if parent == grand_parent.get_left():
                # Rename for ease of implementation
                uncle = grand_parent.get_right()

                # Case 1
                # Check for not None as None is equivalent with black
                if uncle is not None and uncle.is_red():         
                    parent.set_black()
                    uncle.set_black()
                    grand_parent.set_red()
                    node = grand_parent
                else:
                    # Check for Case 2
                    if node == parent.get_right():                           
                        self._left_rotate(parent)
                        parent = node
                        node = node.get_left()

                    # Case 3                          
                    self._right_rotate(grand_parent)                     
                    parent.set_black()
                    grand_parent.set_red()
            
            # Same as above but RIGHT <> LEFT
            else:
                # Rename for ease of implementation                                                       
                uncle = grand_parent.get_left()

                # Case 1
                # Check for not None as None is equivalent with black
                if uncle is not None and uncle.is_red():         
                    parent.set_black()
                    uncle.set_black()
                    grand_parent.set_red()
                    node = grand_parent
                else:
                    # Check for Case 2
                    if node == parent.get_left():                           
                        self._right_rotate(parent)  
                        parent = node
                        node = node.get_right()

                    # Case 3
                    self._left_rotate(grand_parent)                      
                    parent.set_black()
                    grand_parent.set_red()
        
        # Set root to black
        self._root.set_black()

    def _right_rotate(self, node):
        temp = node._left
        node._left = temp._right
        temp._parent = node._parent

        if temp._right is not None:
            temp._right._parent = node
        
        if node._parent is not None:
            if node is node._parent._right:
                node._parent._right = temp
            else:
                node._parent._left = temp
        else:
            self._root = temp

        node._parent = temp
        temp._right = node
        
        

    def _left_rotate(self, node):
        temp = node._right
        node._right = temp._left
        temp._parent = node._parent

        if temp._left is not None:
            temp._left._parent = node

        if node._parent is not None:
            if node is node._parent._left:
                node._parent._left = temp
            else:
                node._parent._right = temp
        else:
            self._root = temp

        node._parent = temp
        temp._left = node
              
    def get(self, key):
        return self._get(self._root,key)
    
    def _get(self,node,key):
        if node is None:
            return []
        if node.get_key() == key:
            return node._values
        else:
            if key < node.get_key():
                return self._get(node.get_left(),key)
            else:
                return self._get(node.get_right(),key)

    # Debug tool to detect nested lists in node._values
    def loop_test(self):
        print('Test Started')
        self._loop_test(self._root)
        print('Test Completed')

    def _loop_test(self, node):
        if node is not None:
            for val in node._values:
                if isinstance(val, list):
                    print('Nested loops in RBtree detected!')
            self._loop_test(node.get_left())
            self._loop_test(node.get_right())