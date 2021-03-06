class Node:
 
    def __init__(self,data):
        self.data = data
        self.next = None
 
class linkedlist:
 
    def __init__(self):
        self.head = None
 
    def insert(self,new_data):
        new_node = Node(new_data)
        if self.head is None :
            self.head = new_node
            return
        last =self.head
        while(last.next):
            last = last.next
 
        last.next = new_node
 
    def showdata(self):
        current = self.head
        while current is not  None :
            print current.data,
            current =current.next
 
    def sortList(self):
        current = self.head
        index = None
 
        if (self.head == None):
            return
        else:
            while (current != None):
                index = current.next
 
                while (index != None):
                    if (current.data > index.data):
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next
 
 
llist1 = linkedlist()
llist1.insert(2)
llist1.insert(4)
llist1.insert(-1)
llist1.insert(0)
llist1.insert(-6)
print "Sebelum Diurut"
llist1.showdata()
print "\n"
print "Sesudah diurut"
llist1.sortList()
llist1.showdata()
