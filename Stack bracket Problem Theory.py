#Stack Bracket Problem Theory:-
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
        
class stack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top == None
        
        
    def push(self,value):
        new_node = Node(value)
        
        new_node.next = self.top
        self.top = new_node
        
    def __str__(self):
        if self.is_empty():
            return 'stack empty'
        res = ''
        curr = self.top
        
        while curr!=None:  

            res += str(curr.data) + '->'
            
            curr = curr.next
            
        return res[:-2]
    
    
    def pop(self):
        data = self.top.data
        self.top = self.top.next
        return data
        
        
    def is_balanced(self,exp):
        for char in exp:
            if '(' == char or '[' == char or '{' == char :
                self.push(char)
                
                
            else:
                if self.is_empty():
                    return False
                
                curr_char = self.pop()
                
                if curr_char == '(':
                    if char != ')':
                        return False
                
                elif curr_char == '[':
                    if char != ']':
                        return False
                
                elif curr_char == '{':
                    if char != '}':
                        return False
                
        if self.is_empty():
            return True
        else:
            return False
            
        
    

        




s = stack()
exp = '{}[]()'
print(s.is_balanced(exp))
