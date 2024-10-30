from collections import deque

queue = deque()
queue.append("customer1") #Enqueue
queue.append("customer2") #Enqueue
first_customer = queue.popleft() #Dequeue
print(first_customer)  #output: 'customer1'
print(queue)  # Output: deque(['customer2'])