class node:
    def __init__(self,val):
        self.val = val
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def printdata(self):
        temp = self.head
        while(temp):
            print(temp.val,end=" ")
            temp=temp.next
    def insertatfront(self,val):
        newnode = node(val)
        if(self.head is None):
            self.head=newnode
            return
        newnode.next = self.head
        self.head = newnode
    def atposition(self,prenode,val):
        newnode = node(val)
        if(self.head.val == prenode):
            newnode.next = self.head
            self.head = newnode
        temp = self.head
        while(temp):
            pre = temp
            if(temp.val == prenode):
                newnode.next = temp.next
                temp.next = newnode
                return
            temp = temp.next
    def deletenode(self,val):
        if(self.head.val == val):
            self.head = self.head.next
            return
        temp = self.head
        while(temp):
            if(temp.val == val):
                break
            pre = temp
            temp = temp.next
        pre.next = temp.next











l1 = linkedlist()
l1.head = node(1)
l2 = node(2)
l3 = node(3)
l4 = node(4)
l1.head.next = l2
l2.next = l3
l3.next = l4
l1.insertatfront(444)
l1.atposition(4,67)
l1.deletenode(3)
l1.printdata()
