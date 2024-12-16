#Celebrity Problem:-

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class stack:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def is_empty(self):
        return self.top == None
        
    def push(self,value):
        new_node = Node(value)
        if self.is_empty():
            self.top = new_node 
            self.size +=1
        
        else:
            new_node.next = self.top 
            self.top = new_node
            self.size +=1
            
    def pop(self):
        
        if self.is_empty():
            return None

        data = self.top.data
        self.size -=1
        self.top = self.top.next
        
        return data 
    
    def traverse(self):
        if self.is_empty():
            return 'stack empty'
        
        curr = self.top
        while curr!=None:
            print(curr.data,end=" ")
            curr = curr.next
            

def find_the_celeb():
    l = [[0,0,1,1],
         [0,0,1,1],
         [1,0,0,0],
         [0,0,1,0]]
    
    for i in range(len(l)):
        s.push(i)
        
    
        
        while s.size >= 2:
            i = s.pop()
            j = s.pop()
            
            if l[i][j] == 0:
                s.push(i)
                
            else:
                s.push(j)
                
                
                
                
    celeb = s.pop()
    print(celeb)
    
    for i in range(len(l)):
        if i != celeb:
            
            if l[i][celeb] == 0 or l[celeb][i] == 1:
                print("No one celebrity")
                return 
    print("the celebrity is",celeb)
        
    
    
    
    
    
    
    #it's working but it's shows not working next week sometime not wokring so working....
    
    
                
        
s = stack()
find_the_celeb()



