# Node class for Circular Linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class JosephusCircle:
    def __init__(self, k):
        self.k = k  # Interval of elimination
        self.head = None

    def add_person(self, value):
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

    def eliminate(self):
        current = self.head
        while current.next != current:
            for _ in range(self.k - 1):  # Move k-1 steps
                current = current.next
            print("Eliminating:", current.next.value)
            current.next = current.next.next  # Eliminate k-th person
        print("Survivor:", current.value)

# Testing Josephus problem
circle = JosephusCircle(3)
circle.add_person("Person 1")
circle.add_person("Person 2")
circle.add_person("Person 3")
circle.add_person("Person 4")
circle.add_person("Person 5")
circle.eliminate()
