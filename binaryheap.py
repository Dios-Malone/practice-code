import pdb

class Heap:
   def __init__(self):
      self.data = []
   def __str__(self):
      return str(self.data)
   
   def _siftup(self, index):
      pdb.set_trace()
      while self._parent(index) is not None and self.data[self._parent(index)] < self.data[index]:
         self._swap(index, self._parent(index))
         index = self._parent(index)
         
   def _siftdown(self, index):
      while self._rightchild(index) and (self.data[self._rightchild(index)] > self.data[index] or self.data[self._leftchild(index)] > self.data[index]):
         if self.data[self._rightchild(index)] > self.data[self._leftchild(index)]:
            self._swap(index, self._rightchild(index))
            index = self._rightchild(index)
         else:
            self._swap(index, self._leftchild(index))
            index = self._leftchild(index)
      if self._leftchild(index) and self.data[self._leftchild(index)] > self.data[index]: #in case of right child not exist
         self._swap(index, self._leftchild(index))
         index = self._leftchild(index)

   def _parent(self, index):
      if index == 0:
         return None
      p_index = (index-1)/2
      return p_index
      
   def _leftchild(self, index):
      leftchild_index = index * 2 + 1
      if leftchild_index < len(self.data):
         return leftchild_index
      else:
         return None
      
   def _rightchild(self, index):
      rightchild_index = index * 2 + 2
      if rightchild_index < len(self.data):
         return rightchild_index
      else:
         return None
         
   def _swap(self, i1, i2):
      assert i1 < len(self.data) and i2 < len(self.data)
      temp = self.data[i1]
      self.data[i1] = self.data[i2]
      self.data[i2] = temp
      
      
   def push(self, node):
      self.data.append(node)
      self._siftup(len(self.data)-1)
      
   def pop(self):
      if len(self.data) == 1:
         return self.data.pop(0)
      elif self.data:
         output = self.data[0]
         self.data[0] = self.data.pop(len(self.data)-1)
         self._siftdown(0)
         return output
      else:
         return None