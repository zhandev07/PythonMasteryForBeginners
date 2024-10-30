class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Method to reverse the doubly linked list
    def reverse(self):
        current = self.head
        temp = None
        while current:
            # Swap the next and prev pointers
            temp = current.prev
            current.prev = current.next
            current.next = temp
            # Move to the next node (previously the next node)
            current = current.prev
        if temp:
            self.head = temp.prev  # Update head to the new first node

    # Display list forward
    def display_forward(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

# Testing reverse method
dll = DoublyLinkedList()
dll.insert_at_end("Song 1")
dll.insert_at_end("Song 2")
dll.insert_at_end("Song 3")
dll.reverse()
dll.display_forward()
