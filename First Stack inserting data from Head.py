#Inserting from Head As Operation (push) In Stack:-

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
    
class stack:
    def __init__(self):
        self.top = None
        
        
    def isempty(self):
        return self.top == None 
        
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        
        self.top = new_node
        
        
    def traverse(self):
        
        temp = self.top
        
        while temp!=None:
            print(temp.data)
            temp = temp.next
            
s = stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)

s.traverse()
