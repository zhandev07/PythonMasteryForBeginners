# Step 1: Define a Node
class Node:
    def __init__(self, value):
        self.value = value  # Store data
        self.next = None    # Store reference to the next node

# Step 2: Define a LinkedList
class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    # Method to add a new node to the end of the list
    def append(self, value):
        new_node = Node(value)  # Create a new node
        if not self.head:       # If list is empty, make new node the head
            self.head = new_node
            return
        # Otherwise, find the last node
        current = self.head
        while current.next:
            current = current.next  # Move to the next node
        # Link the last node to the new node
        current.next = new_node

    # Method to print the list
    def display(self):
        current = self.head
        while current:  # Traverse till the end of the list
            print(current.value, end=" -> ")
            current = current.next
        print("None")  # Mark the end of the list

# Testing the LinkedList
linked_list = LinkedList()
linked_list.append("Node 1")  # Add first node
linked_list.append("Node 2")  # Add second node
linked_list.append("Node 3")  # Add third node
linked_list.display()

# 1. Insertion
# Method to insert a node at the beginning
def insert_at_beginning(self, value):
    new_node = Node(value)  #Create a new node
    new_node.next = self.head # Link new node the current
    self.head = new_node   # Update head to new node

# Adding the method to LinkedList class
LinkedList.insert_at_beginning = insert_at_beginning

# Testing insert_at_biggeiner
linked_list.insert_at_beginning("Node 0")
linked_list.display()

# 2. Deletion 

# Method to delete a node by value
def delete_node(self, value):
    current = self.head

    # If the node to be deleted is the heaf
    if current and current.value == value:
        self.head = current.next
        current = None
        return
    
    # Otherwise, search fo the node to be deleted
    prev = None
    while current and current.value != value:
        prev = current
        current = current.next

    # If the node was not founf
    if current is None:
        return
    
    # Unlink the node from the list
    prev.next = current.next
    current = None

# Adding the method to LinkedList class
LinkedList.delete_node = delete_node

# Testing delete_node
linked_list.delete_node("Node 2")
linked_list.display()



# 3. Searching

# search for a node by value
# def search(self, value):
#     current = self.head
#     position = 0
#     while current:
#         if current.value == value:
#             print(f"Value '{value}' found at position '{position}'")
#             return
#         current = current.next
#         position += 1
#     print(f"Value '{value}' not found in the list")

# linked_list = LinkedList()
# linked_list.search("Node 1")
# linked_list.search("Node 0")


# 4. Reversing
# Reverse the linked list
# def reverse(self):
#     prev = None
#     current = self.head
#     while current:
#         next_node = current.next #save next
#         current.next = prev #reverse the pointer
#         prev = current #move prev to current
#         current = next_node # move to next_node
#     self.head = prev # Reset head to new front of list

# # Testing reversing a singly linked list
# sll = LinkedList()
# sll.append("Node 1") 
# sll.append("Node 2") 
# sll.append("Node 3")  
# print("Original List:")
# sll.display()
# sll.reverse()
# print("Reversed List:")
# sll.display()