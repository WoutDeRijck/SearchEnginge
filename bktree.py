# Group 43; Tuytte Victor; De Rijck Wout

from queue import LifoQueue

class BKTreeNode():
    
    def __init__(self, key):
        self._key = key
        self._children = {} # length as key, child as value

class BKTree():
    
    def __init__(self, distance_function):
        self._root = None
        self._count = 0
        self._distance_function = distance_function
        
    def __len__(self):
        return self._count
        
    def insert(self, key):
        # Init
        loop = True
        dist = self._distance_function
        current_node = self._root

        # Is BKtree empty?
        if current_node is None:
            self._root = BKTreeNode(key)
            self._count += 1
            return

        # Search for correct place of key
        while loop:
            k = dist(current_node._key, key)

            # Check for doubles
            if k == 0:
                return

            child = current_node._children.get(k, None)

            # Does child exist?
            if child is not None:
                current_node = child
            else:
                # Update count & BKtree and exit loop
                current_node._children.update({k:BKTreeNode(key)})
                self._count += 1
                loop = False
                    
    def get(self, key, max_dist = 1):
        # Init
        current_node_queue = LifoQueue()
        current_node_queue.put(self._root)
        dist = self._distance_function
        words = []

        # Search while there are nodes to be searched
        while not current_node_queue.empty():

            # Pop current_node
            current_node = current_node_queue.get()
            k = dist(current_node._key, key)

            # Go over relevant distances
            for i in range(k-max_dist, k+max_dist+1, 1):
                child = current_node._children.get(i)

                # Does child exist?
                if child is not None:
                    d = dist(child._key, key)
                    if d <= max_dist:
                        words.append((child._key,d))

                    # Append node to search
                    current_node_queue.put(child)
                    
        return words