class Node:
    def __init__(self,value):
        self.data = value
        self.next = None  

class LinkedList:

    #__init__ method initializes the head of the list as None.
    def __init__(self):
        self.head = None

    """ Append a node with the given data to the end of the list. """
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Added new Node as head with value {data}")
            return
        
        # Intialize the current node to head 
        last_node = self.head

        # while the current node is not None keep moving to the next node
        while last_node.next:
            last_node = last_node.next
        # While loops exists at the last node now assign new node to the current node
        last_node.next = new_node
        print(f"Added new Node with value {data}")

    """ Prepend a node with the given data to the start of the list. """
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Prepended Node with value {data}")
    
    """ Traverse the list and print each node's data. """
    def traverse(self):
        print("Our current linked list is as follows:")
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    """ Delete the first occurence node with the given data. """
    def delete_node(self,data):
        ## Check if head is empty
        if not self.head:
            return
        
        ## Check if head contains the data to be deleted
        if self.head.data == data:
            self.head = self.head.next
            return
        
        ## Take a temporary node as head
        temp_node = self.head
            
        while (temp_node is not None):
            prev = temp_node
            current = prev.next
            if current.data == data:
                # delete the node making previous node link to next node
                print(f"Deleting node with value {current.data}")
                prev.next = current.next 
                break
            temp_node = temp_node.next    
        
if __name__ == '__main__':
    l1 = LinkedList()
    l1.append(10)
    l1.append(20)
    l1.append(30)
    l1.append(40)
    l1.append(50)
    l1.prepend(34)
    l1.traverse()
    l1.delete_node(20)
    l1.traverse()
    l1.delete_node(40)
    l1.traverse()
