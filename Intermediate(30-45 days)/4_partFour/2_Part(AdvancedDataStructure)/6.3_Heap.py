import heapq

# Min-Heap
min_heap = []
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 20)
print(heapq.heappop(min_heap))  # Output: 5
