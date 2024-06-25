class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next  # Save the next node
            current_node.next = prev_node  # Reverse the link
            prev_node = current_node       # Move prev to current
            current_node = next_node       # Move current to next node
        self.head = prev_node  # Update the head to the new first node
        

    
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
    ls.traverse()
    ls.reverse()
    ls.traverse()


""" This implementation efficiently reverses the linked list in place, with a time complexity of 𝑂(𝑛)where 𝑛 is the number of nodes in the list, and a space complexity of 𝑂(1)."""


