# Author: Gabriel Tinsley
# Date: 4/20/2025
# Description: Extends model so that some bots act as sub-commanders, forming trees

# botnet_hierarchical.py
class Bot:
    def __init__(self, bot_id):
        self.bot_id = bot_id
        self.sub_bots = []

    def add_sub_bot(self, bot):
        self.sub_bots.append(bot)

    def receive_command(self, command):
        print(f"[Bot {self.bot_id}] Received command: {command}")
        for bot in self.sub_bots:
            bot.receive_command(command)

# Create hierarchy
root = Bot("Root")
layer1_a = Bot("A")
layer1_b = Bot("B")
layer2_1 = Bot("A1")
layer2_2 = Bot("B1")

layer1_a.add_sub_bot(layer2_1)
layer1_b.add_sub_bot(layer2_2)
root.add_sub_bot(layer1_a)
root.add_sub_bot(layer1_b)

root.receive_command("scan_network")
