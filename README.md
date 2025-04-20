# Lab03-CS331-Gabriel_Tinsley

### Observations
botnet_centralized:
    * The C&C server is the only thing in charge, the bots do NOT speak to eachother
    * Removing the server makes the whole botnet useless
    * One bot failing really does not effect much

botnet_hierarchical:
    * The bots speak to eachother based on authority (root has most authority)
    * Added a check to make sure no bot can speak to a bot on a higher level (throws Error)
    * Heavily dependent of root node that holds a bot

botnet_p2p:
    * The bots speak to eachother in a certain order, similar to a singly-linked list
    * The node order matters a lot, just switching up the order can make a big difference
    * Bots can be "unreachable" if not added in correct order

### Limitations
This is a simulation of real world networked servers, so the server is a logical controller. The limitation of this is the real world factor, even though this was
suppose to be as realistic as possible, there is still a way to make this way better, by doing a real world implementation.

### How to Run Script
From the directory containing all source files, compile the driver class (and all dependencies), and run the program with the command:
> python .\botnet_centralized.py

* This will output 100 bots, all reading the command "launch_ddos" from the C&C server

From the directory containing all source files, compile the driver class (and all dependencies), and run the program with the command:
> python .\botnet_hierarchical.py

* This will show 1 Error and then the root bot communicating too all the bots below itself

From the directory containing all source files, compile the driver class (and all dependencies), and run the program with the command:
> python .\botnet_p2p.py

* This will show bot 0 recieving a message and communicating to bot 1. To allow more bots to communicate change the neighbors of the bots.
