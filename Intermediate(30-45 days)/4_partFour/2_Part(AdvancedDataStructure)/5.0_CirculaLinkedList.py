# Node class for Circular Linked list
class Cnode:
    def __init__(self, value):
        self.value = value
        self.next = None


# Circular Linked list class
class CircularLinkedList():
    def __init__(self):
        self.head = None

    # Method to add new node at the end 
    def append(self, value):
        new_node = Cnode(value)
        if not self.head:  # if list is empty
            self.head = new_node
            new_node.next = self.head # point to itself
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head # complete the circular

    # Method to display the list in a circular way
    def display(self):
        if not self.head:
            print("list is empty")
            return
        current = self.head
        while True:
            print(current.value, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("Back to head")

# Testing the circular Linked List
circular_linked_list = CircularLinkedList()
circular_linked_list.append("Node 1")
circular_linked_list.append("Node 2")
circular_linked_list.append("Node 3")
circular_linked_list.append("Node 4")
circular_linked_list.display()