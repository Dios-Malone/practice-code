
class Node:
   def __init__(self, value):
      self.value = value
      self.parent = None
      self.left = None
      self.right = None
      
   def setleft(self, left):
      self.left = left
      
   def setright(self, right):
      self.right = right
      
      
class BST:
   def __init__(self, l = None):
      self.root = None
      if l and isinstance(l, list):
         for item in l:
            self.insert(item)
   
   def insert(self, item):
      try:
         item > item
      except TypeError as e:
         raise TypeError('Non-comparable item is not supported')
      if self.root is None:
         self.root = Node(item)
      elif self.root.value > item:
         if self.root.left:
            self._insert2node(item, self.root.left)
         else:
            self.root.left = Node(item)
      else:
         if self.root.right:
            self._insert2node(item, self.root.right)
         else:
            self.root.right = Node(item)
      
   def _insert2node(self, item, node):
      if node.value > item:
         if node.left:
            self._insert2node(item, node.left)
         else:
            node.left = Node(item)
      else:
         if node.right:
            self._insert2node(item, node.right)
         else:
            node.right = Node(item)
            
   def getSortedList(self):
      result = []
      self._visitnode(self.root, result)
      return result
      
   def _visitnode(self, node, l):
      if node.left:
         self._visitnode(node.left, l)
      l.append(node.value)
      if node.right:
         self._visitnode(node.right, l)
         
def treesort(items):
   bst = BST(items)
   return bst.getSortedList()
      
         
   
test_input = [12,32,14,2,43,156,78,47,13,34, 0, 109]

print(treesort(test_input))
      