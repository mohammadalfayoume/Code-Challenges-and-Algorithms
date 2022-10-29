# Write here the code challenge solution

class Queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self,val):
        self.s1.append(val)

    def pop(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        pop_val = self.s2.pop()

        while self.s2:
            self.s1.append(self.s2.pop())
        
        return pop_val

    def peek(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        peek_val = self.s2[-1]

        while self.s2:
            self.s1.append(self.s2.pop())
        
        return peek_val

    def empty(self):
        if not self.s1 and not self.s2:
            return True
        else:
            return False



# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None

# class Stack:
#     def __init__(self):
#         self.first=None
#         self.last=None
#         self.size=0
#         self.list=[]
    
#     def push(self,value):
#         new_node= Node(value)
        
#         if not self.first:
#             self.first=new_node
#             self.last=new_node
#         else:
#             new_node.next=self.first
#             self.first=new_node
#         self.list.append(self.first.value)
#         self.size +=1
#         return self.list
        
#     def pop(self):
#         if not self.first:
#             return "Empty stack"
#         if self.first==self.last:
#             self.last=None
#         temp= self.first
#         self.first=self.first.next
#         self.size -=1
#         return temp.value
    
#     def peek(self):
#         if not self.empty():
#             return self.first.value
#         else:
#             return "Empty"

#     def empty(self):
#         if not self.first:
#             return True
#         else:
#             return False





# class Queue:
#     def __init__(self):
#         self.first=None
#         self.last=None
#         self.size=0
    
    
#     def push(self,value):
#         new_node= Node(value)
#         if not self.first: # if the queue was empty
#             self.first=new_node
#             self.last=new_node
        
#         else:
#             self.last.next=new_node
#             self.last=new_node
#         self.size +=1
#         return new_node.value

#     def pop(self):
#         temp= self.first
#         if not self.first:
#             return "Empty"
#         else:
#             self.first=self.first.next
#         self.size -=1
#         return temp.value
    
#     def peek(self):
#         return self.first
    
#     def empty(self):
#         if not self.first:
#             return True
#         else:
#             return False
