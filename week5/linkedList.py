class DoublyLinked:
    class Node:
        def __init__(self, data, next=None, prev=None):
            self._data = data
            self._next = next
            self._prev = prev  

        def get_data(self):
            return self._data

        def get_next(self):
            return self._next

        def get_previous(self):
            return self._prev  
    def __init__(self):
        self._front = None
        self._back = None

    def get_front(self):
        return self._front

    def get_back(self):
        return self._back
#push_front
    def push_front(self, data):
        new_node = self.Node(data, self._front)  
        if self._front is None:
            self._front = self._back = new_node
        else:
            self._front._prev = new_node
            self._front = new_node
# push with double linked 
    def push_back(self, data):
        new_node = self.Node(data, None, self._back)  

        if self._back is None:
            self._front = self._back = new_node  
        else:
            self._back._next = new_node  
            self._back = new_node

    def pop_front(self):
        if self._front is None:
            raise IndexError('pop_front() used on empty list')
        
        data = self._front.get_data()
        if self._front == self._back:
            self._front = self._back = None
        else:
            self._front = self._front._next
            self._front._prev = None
        return data  
# pop _front
    def pop_back(self):
        if self._back is None:
            raise IndexError('pop_back() used on empty list')
        
        data = self._back.get_data()
        if self._front == self._back:
            self._front = self._back = None  
        else:
            self._back = self._back.get_previous()
            self._back._next = None
        return data

#there are two 2 (front, back sentinal)
class Sentinel:
    class Node:
        #this is the first
        def __init__(self, data=None, next=None, prev=None):  # Added default None for data
            self._data = data
            self._next = next
            self._prev = prev

        def get_data(self):
            return self._data

        def get_next(self):
            return self._next

        def get_previous(self):
            return self._prev

    def __init__(self):
        self._sentinel = self.Node()  
        self._sentinel._next = self._sentinel
        self._sentinel._prev = self._sentinel

    def get_front(self):
        if self._sentinel._next == self._sentinel: 
            return None
        return self._sentinel._next

    def get_back(self):
        if self._sentinel._prev == self._sentinel:
            return None
        return self._sentinel._prev
# push back of the data
    def push_front(self, data):
        #define 
        new_node = self.Node(data, self._sentinel._next, self._sentinel)  
        self._sentinel._next._prev = new_node  
        self._sentinel._next = new_node

    def push_back(self, data):
        new_node = self.Node(data, self._sentinel, self._sentinel._prev)  
        self._sentinel._prev._next = new_node
        self._sentinel._prev = new_node

    def pop_front(self):
        if self._sentinel._next == self._sentinel:
            raise IndexError('pop_front() used on empty list')
        
        front_node = self._sentinel._next
        data = front_node.get_data()
        self._sentinel._next = front_node._next
        front_node._next._prev = self._sentinel
        return data

    def pop_back(self):
        if self._sentinel._prev == self._sentinel:
            raise IndexError('pop_back() used on empty list')
        
        back_node = self._sentinel._prev
        data = back_node.get_data()
        self._sentinel._prev = back_node._prev
        back_node._prev._next = self._sentinel
        return data