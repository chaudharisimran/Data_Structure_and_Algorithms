class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):

        # Create a new Node with the given data
        new_node = Node(data)

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

    def traverse(self):
        current_node = self.head
        print("Our current linked list is as follows:")
        while current_node:
            print(current_node.data , end=" --> ")
            current_node = current_node.next
        print("None")



if __name__ == "__main__":
    ls = LinkedList()
    ls.append(54)
    ls.append(45)
    ls.append(15)
    ls.append(65)
    ls.append(90)
    ls.prepend(32)
    ls.traverse()



