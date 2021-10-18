# Group 43; Tuytte Victor; De Rijck Wout

class BinaryTreeNode():
    
    def __init__(self, key, value, left = None, right = None):
        self._key = key
        self._values = [value]
        self._left = None
        self._right = None
        
    def get_key(self):
        return self._key
    
    def get_values(self):
        return self._values

    def add_value(self, value):
        self._values.append(value)
        
    def set_right(self, node):
        self._right = node
        
    def set_left(self, node):
        self._left = node
        
    def get_right(self):
        return self._right
    
    def get_left(self):
        return self._left
 

class BinaryTree():
    
    def __init__(self):
        self._root = None
        self._count = 0
        
    def __len__(self):
        return self._count
        
    def insert(self, key, value):
        if self._root is None:
            self._root = BinaryTreeNode(key, value)
            self._count = 1
        else:
            self._insert(self._root,key, value)
                      
    def get(self, key):
        return self._get(self._root,key)
        
    def _insert(self, node, key, value):
        if node.get_key() == key:
            node.add_value(value)
        else:
            if  key < node.get_key():
                if node.get_left() is None:
                    node.set_left(BinaryTreeNode(key,value))
                    self._count += 1
                else:
                    self._insert(node.get_left(),key,value)
            else:
                if node.get_right() is None:
                    node.set_right(BinaryTreeNode(key,value))
                    self._count += 1
                else:
                    self._insert(node.get_right(),key,value)
    
    def _get(self,node,key):
        if node is None:
            return None
        if node.get_key() == key:
            return node._values
        else:
            if key < node.get_key():
                return self._get(node.get_left(),key)
            else:
                return self._get(node.get_right(),key)
