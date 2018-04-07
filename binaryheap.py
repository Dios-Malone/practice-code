import pdb

class Heap:
   def __init__(self, list = []):
      self.data = list
      self.size = len(self.data)
      self._heapify()
   
   def _heapify(self):
      start = self._parent(self.size - 1)
      while start >= 0:
         self._siftdown(start)
         start -= 1
         
   def __str__(self):
      return str(self.data)
   
   def _siftup(self, index):
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
      p_index = (index-1)//2
      return p_index
      
   def _leftchild(self, index):
      leftchild_index = index * 2 + 1
      if leftchild_index < self.size:
         return leftchild_index
      else:
         return None
      
   def _rightchild(self, index):
      rightchild_index = index * 2 + 2
      if rightchild_index < self.size:
         return rightchild_index
      else:
         return None
         
   def _swap(self, i1, i2):
      assert i1 < self.size and i2 < self.size
      temp = self.data[i1]
      self.data[i1] = self.data[i2]
      self.data[i2] = temp
      
      
   def push(self, node):
      self.data.append(node)
      self._siftup(self.size-1)
      
   def pop(self):
      if self.size == 1:
         return self.data.pop(0)
      elif self.data:
         output = self.data[0]
         self.data[0] = self.data.pop(self.size-1)
         self._siftdown(0)
         return output
      else:
         return None
         
   def sort(self):
      count = self.size - 1
      while count > 0:
         self._swap(0, count)   # 1. swap first element with last element
         self.size -= 1         # 2. reduce the heap range. The remaining list becomes sorted list
         self._siftdown(0)      # 3. reshape the heap so that it fulfill the heap property again.
         count -= 1             # 4. repeat step 1-3 until the heap size becomes 0 and the sorted list size becomes the original list size.
      return self.data
         
         
def heapsort(list):
   h = Heap(list)
   print(h.sort())
   
test_list = [3,24,52,34434,123,43,243,65,2,454,765,345,36,675,345,24,45,54,45,0,54]
heapsort(test_list)
   