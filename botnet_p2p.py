# Author: Gabriel Tinsley
# Date: 4/20/2025
# Description: Create a decentralized botnet where bots foward commands among neighbors

# botnet_p2p.py
class Bot:
    def __init__(self, bot_id):
        self.bot_id = bot_id
        self.neighbors = []

    def connect(self, other):
        self.neighbors.append(other)

    def receive_command(self, command, visited=None):
        if visited is None:
            visited = set()
        if self.bot_id in visited:
            return
        visited.add(self.bot_id)
        print(f"[Bot {self.bot_id}] Executing: {command}")
        for neighbor in self.neighbors:
            neighbor.receive_command(command, visited)

# Create mesh
bots = [Bot(i) for i in range(5)]
bots[0].connect(bots[1])
bots[1].connect(bots[2])
bots[2].connect(bots[3])
bots[3].connect(bots[4])
bots[4].connect(bots[0])  # cycle

bots[0].receive_command("update_config")
