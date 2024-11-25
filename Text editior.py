#Text editor using stack:-

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
        
    def pop(self):
        #it' remove a last item those on top of stack "LIFO"
        if self.isempty():
            return 'stack empty'
        
        else:
            data = self.top.data
            self.top = self.top.next
            
        return data
            
    def traverse(self):
        
        if self.isempty():
            print('stack empty')
        
        curr = self.top
        
        while curr!=None:
            print(curr.data)
            curr = curr.next
            
class Text_editor():   
    def __init__(self):
        self.u = stack()
        self.r = stack()
        
         
    def txt_editior(self,text,pattern):
        
        for char in text:
            self.u.push(char)
            
        for word in pattern:
            if word == "u":
                data = self.u.pop()

                self.r.push(data)
            else:
                data = self.r.pop()
                
                self.u.push(data)
                
        result = ''
        
        while not self.u.isempty():

            result = self.u.pop() + result 
            
        print("Output:",result)
        
    
    
            
        
    
   

                    
s = Text_editor()
s.txt_editior("hello","uruuu")


                    