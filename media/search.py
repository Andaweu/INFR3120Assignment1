from my_queue import Queue
from my_stack import Stack
import networkx as nx
import matplotlib.pyplot as plt

def BFS(graph, root):
    """
    Performs a Breadth-First Search on a given graph
    to output a spanning subgraph of the original graph,
	and the sequence of nodes are visited.
    """
    #Your code here


    visitedNodes = set() #creates a set for visited nodes
    queue = Queue() #creates a queue from the class my_queue.py
    sequence = [] #list to store the sequence of the nodes
    spanningTree = nx.Graph() 

    queue.push(root) #sets the root node as the first value in queue
    visitedNodes.add(root) #adds the root node to visited node
    while not queue.is_empty(): #runs until the queue is empty
        pointer = queue.pop() #pops the first item in the queue and points to it
        sequence.append(pointer) #adds the pointed item to the sequence of visited nodes
        
        for i in graph.neighbors(pointer):
            if i not in visitedNodes: #for a node not in previously visited node
                visitedNodes.add(i) #mark the node as visited
                queue.push(i) #pushes the current node to the queue
                spanningTree.add_edge(pointer, i) #adds an edge to the graph for the pointers location
    return spanningTree, sequence #returns the graph and the BFS sequence


    


def DFS(graph, root):
    """
    Performs a Depth-First Search on a given graph starting
	from root node to output a spanning subgraph of the
	original graph, the sequence of visited nodes.
    """
    #Your code here

    visitedNode = set() #creates a set for visited nodes
    stack = Stack() #creates a stack from the class my_stack.py
    sequence = [] #list to store the sequence of the nodes
    spanningTree = nx.Graph()

    stack.push(root) #sets the root as the first value in the stack
    visitedNode.add(root) #marks the root as the first node visited
    while not stack.is_empty(): #runs while the stack is not empty
        pointer = stack.pop() #pops the last item in the stack and points to it
        sequence.append(pointer) #appends the pointer to the sequence of nodes

        for i in reversed(list(graph.neighbors(pointer))): #because a stack is used (LIFO) the list is reversed
            if i not in visitedNode: #if the node has not been visited yet
                visitedNode.add(i) #marks the current node as visited
                stack.push(i) #pushes the current node to the stack
                spanningTree.add_edge(pointer, i) #adds an edge to the graph for the current location
    return spanningTree, sequence #returns the graph and the DFS sequence

def show_graph(graph):
    plt.subplot(111)
    pos = nx.spring_layout(graph, seed=11)
    nx.draw(graph, with_labels=True, font_weight='bold', pos=pos)
    plt.show()

def create_tree():
    g = nx.Graph()
    for i in range(7):
        source = i if i != 3 else 0
        g.add_edge(source, i+1)
    return g


graph = nx.erdos_renyi_graph(12, 0.25, seed=42)

show_graph(graph)
BFSspan, BFSseq = BFS(graph, 0)
DFSspan, DFSseq = DFS(graph, 0)

print ("BFS Seguence: ", BFSseq)
print ("DFS Seguence: ", DFSseq)
show_graph(graph)

graph =  create_tree()
show_graph(graph)
BFSspan, BFSseq = BFS(graph, 0)
DFSspan, DFSseq = DFS(graph, 0)

print ("BFS Seguence: ", BFSseq)
print ("DFS Seguence: ", DFSseq)
show_graph(graph)


