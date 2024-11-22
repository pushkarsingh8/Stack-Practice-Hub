#Reversed String using Stack:-
class Node:
    
    def __init__(self,value):
        self.data = value
        self.next = None
        
        
class stack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top == None
        
    def traverse(self):
        
        if self.is_empty():
            print('stack empty')
        
        curr = self.top
        
        while curr!=None:
            print(curr.data)
            curr = curr.next
             
            
    def pop(self):
        #it' remove a last item those on top of stack "LIFO"
        if self.is_empty():
            return 'stack empty'
        
        else:
            self.top = self.top.next
            
            
        
        
        
    def push(self,value):
        new_node = Node(value)
        if self.is_empty():
            self.top = new_node
        
        else:
            new_node.next = self.top
            self.top = new_node
            
            
        
        
        
s = stack()
for i in range(1,10):
    s.push(i)

