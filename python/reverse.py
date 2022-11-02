class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def append(self,value):
        '''
        input -> int or string

        return -> None
        '''
        new_node= Node(value)
        if self.head==None:
            self.head=new_node
        else:
            current=self.head
            while current.next != None:
                current=current.next
            current.next=new_node
        self.length +=1
        
    def reverse(self):
        prev=None
        curr=self.head
        next=self.head
        while curr!=None:
            next=next.next
            curr.next=prev
            prev=curr
            curr=next         
        self.head= prev
                
    def __str__(self):
        '''
        input -> None

        return -> list
        '''
        values_in_list=""
        if self.head==None:
            print("empty linked list")
        else:
            current=self.head
            while current != None:
                # print(current.value)
                if current.next==None:
                    values_in_list += f" => {current.value}"
                    values_in_list += f" => {current.next}"
                else:
                    values_in_list += f" => {current.value}"
                current=current.next
            # print(self.length)
        values_in_list= values_in_list[4:]
        return values_in_list
    
l=LinkedList()
l.append(1)
l.append(2)
l.append(3)

print(l.__str__())

l.reverse()
print(l.__str__())

