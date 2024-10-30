class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    # Display circular linked list
    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.value, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(head)")

# Testing circular linked list insertion
cll = CircularLinkedList()
cll.insert_at_end("Seat 1")
cll.insert_at_end("Seat 2")
cll.insert_at_end("Seat 3")
cll.display()
