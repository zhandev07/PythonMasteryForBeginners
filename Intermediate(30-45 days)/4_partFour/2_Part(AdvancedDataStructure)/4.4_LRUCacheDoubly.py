from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)  # Mark as recently used
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # Move to end as recently used
        self.cache[key] = value
        if len(self.cache) > self.capacity:  # Exceeding capacity
            self.cache.popitem(last=False)  # Remove least recently used item

# Testing LRU Cache
lru = LRUCache(2)  # Capacity of 2
lru.put(1, "Page 1")
lru.put(2, "Page 2")
print(lru.get(1))  # Output: Page 1
lru.put(3, "Page 3")  # Removes key 2
print(lru.get(2))  # Output: -1 (not found)
