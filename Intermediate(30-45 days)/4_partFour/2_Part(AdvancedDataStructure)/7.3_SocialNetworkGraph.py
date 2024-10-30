from collections import deque


class SocialNetwork:
    def __init__(self):
        self.network = {}

    def add_user(self, user):
        if user not in self.network:
            self.network[user] = []

    def add_friendship(self, user1, user2):
        self.network[user1].append(user2)
        self.network[user2].append(user1)

    def find_connections(self, user, level=1):
        visited = set()
        queue = deque([(user, 0)])  # (user, distance from start)
        visited.add(user)
        connections = []

        while queue:
            current_user, depth = queue.popleft()

            # Skip users who are beyond the specified level
            if depth > level:
                break
            
            # Append only friends within the level range
            if depth > 0:
                connections.append(current_user)

            for friend in self.network[current_user]:
                if friend not in visited:
                    visited.add(friend)
                    queue.append((friend, depth + 1))
        
        return connections

# Create network and add friendships
network = SocialNetwork()
network.add_user("Python")
network.add_user("Php")
network.add_user("Java")
network.add_user("Ruby")
network.add_user("C++")

network.add_friendship("Python", "Php")
network.add_friendship("Python", "Java")
network.add_friendship("Php", "Ruby")
network.add_friendship("Java", "C++")

# Find friends within level 2 of Python
print("Connections within level 2 of Python:", network.find_connections("Python", level=2))
