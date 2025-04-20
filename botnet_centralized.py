# Author: Gabriel Tinsley
# Date: 4/20/2025
# Description: Creates a central C&C server connecting bots to the server, and the C&C sends commands to all bots, and logs command delivery.

# botnet_centralized.py
class Bot:
    def __init__(self, bot_id):
        self.bot_id = bot_id

    def receive_command(self, command):
        print(f"[Bot {self.bot_id}] Executing command: {command}")

class CommandServer:
    def __init__(self):
        self.bots = []

    def register_bot(self, bot):
        self.bots.append(bot)

    def send_command(self, command):
        print(f"[C&C] Sending command '{command}' to all bots...")
        for bot in self.bots:
            bot.receive_command(command)

# Simulate
server = CommandServer() # saw what happens when C&C server is removed
for i in range(100): # added a lot more bots
    server.register_bot(Bot(i))

server.send_command("launch_ddos")
