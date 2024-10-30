# Node class for Circular Linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
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

    def round_robin(self, rounds):
        current = self.head
        for _ in range(rounds):
            print("Executing task:", current.value)
            current = current.next

# Testing round-robin scheduling
tasks = CircularLinkedList()
tasks.insert("Task A")
tasks.insert("Task B")
tasks.insert("Task C")
tasks.round_robin(5)
