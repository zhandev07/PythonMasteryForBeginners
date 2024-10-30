# Node class for Doubly Linked List

class Dnode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# Doubly Linked list class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Methd to add new node at the end
    def append(self, value):
        new_node = Dnode(value)
        if not self.head: # if list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node # Update tail to new node

    # Method to display the list forward
    def display_forward(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    # Method to display the list backward
    def display_backward(self):
        current = self.tail
        while current:
            print(current.value, end=" <-> ")
            current = current.prev
        print("None")

# Testing the Doubly Linked List
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append("Node 1")
doubly_linked_list.append("Node 2")
doubly_linked_list.append("Node 3")

# Display list forward and backwar
print("Forward tranversal:")
doubly_linked_list.display_forward()
print("Backward tranversal: ")
doubly_linked_list.display_backward()