class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    # Display list forward
    def display_forward(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    # Delete a node by value
    def delete_by_value(self, value):
        current = self.head
        while current and current.value != value:
            current = current.next
        if not current:
            print("Value not found.")
            return
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.head:  # If deleting the head node
            self.head = current.next

# Testing deletion in doubly linked list
dll = DoublyLinkedList()
dll.insert_at_beginning("Page 1")
dll.insert_at_end("Page 2")
dll.insert_at_end("Page 3")
dll.delete_by_value("Page 2")
dll.display_forward()
