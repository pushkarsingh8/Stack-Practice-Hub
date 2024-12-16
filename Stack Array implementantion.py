#stack Array Implentation:-

class Stack:
    
    def __init__(self,size):
        self.size = size
        self.__stack = [None] *self.size 
        self.top = -1
        
        
    def push(self,value):
        if self.top == self.size -1 :
            return "stack overflow"
            
        else:
            self.top+=1
            self.__stack[self.top] = value
            
            
    def pop(self):
        if self.top == -1:
            return 'stack empty'
        else:
            self.top-=1
            print(self.__stack[self.top])
            
            
    def traverse(self):
        for i in range(self.top+1):
            print(self.__stack[i],end=" ")
            
            
    def peek(self):
        return self.__stack[self.top]
                                     
        
#size given by object [Fixed size] like Array        
s = Stack(10)

for i in range(1,6):
    s.push(i)

s.pop() #delete a top value on top of stack
s.traverse() #traverse in Stack using loop
s.peek() #return only top value in Stack