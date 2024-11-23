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
            data = self.top.data
            self.top = self.top.next
            
        return data
            
        
        
        
    def push(self,value):
        new_node = Node(value)
        if self.is_empty():
            self.top = new_node
        
        else:
            new_node.next = self.top
            self.top = new_node
            
    
    def reverse(self,text):
    
        
        
        for word in text:
            self.push(word)
            # print(word)
            
        
        result = ''
        
        while not self.is_empty():
            result  +=  self.pop() 

            
        print(result)
            
            
            
            
            
        
            
            
        
        
        
s = stack()


    
s.reverse('hello')

