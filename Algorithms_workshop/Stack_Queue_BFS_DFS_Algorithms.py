import networkx as nx

class Stack:
    def __init__(self, stack_size = 10):
        self.stack_size = stack_size
        self.stack_ptr = -1
        self.stack = []
        
    def is_empty(self):
        return self.stack_ptr < 0
    
    def is_full(self):
        return self.stack_ptr > self.stack_size-1
    
    def push(self, data):
        self.stack_ptr += 1
        if self.is_full():
            raise IndexError("out of stack size")
        self.stack.append(data)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("out of stack size")
        self.stack_ptr -= 1
        return self.stack.pop()
    
    def get(self):
        return self.stack
    
class Queue:
    def __init__(self, queue_size = 10):
        self.queue_size = queue_size
        self.end_ptr = -1
        self.queue = []
        
    def is_empty(self):
        return self.end_ptr == -1
    
    def is_full(self):
        return self.end_ptr == self.queue_size
    
    def push(self, data):
        self.end_ptr += 1
        if self.is_full():
            raise IndexError("out of queue size")
        self.queue.append(data)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("out of queue size")
        self.end_ptr -= 1
        return self.queue.pop(0)
    
    def get(self):
        return self.queue

def dfs(graph, start):    
    visited = []
    list_of_nodes = list(graph.keys())
    stack = Stack(len(list_of_nodes))
    visited.append(start)
    print("Start ==> ", start)
    print("visited = ", visited)
    while(True):
        for node in graph.get(start):
            if node not in visited:
                stack.push(node)
        print("Stack ==> ", stack.get(), "\n==============================")
        while not stack.is_empty():
            poped = stack.pop()
            if poped not in visited:
                visited.append(poped)
                start = poped
                print("Poped ==> ", poped)
                break
        if stack.is_empty():
            break
        print("visited = ", visited)
        
def bfs(graph, start):    
    visited = []
    list_of_nodes = list(graph.keys())
    queue = Queue(len(list_of_nodes))
    visited.append(start)
    print("Start ==> ", start)
    print("visited = ", visited)
    while(True):
        for node in graph.get(start):
            if node not in visited:
                queue.push(node)
        print("Queue ==> ", queue.get(), "\n==============================")
        while not queue.is_empty():
            poped = queue.pop()
            if poped not in visited:
                visited.append(poped)
                start = poped
                print("Poped ==> ", poped)
                break
        if queue.is_empty():
            break
        print("visited = ", visited)

def main():
    graph = {'a' : ['b', 'c', 'e'],
         'b' : ['a', 'd'],
         'c' : ['a', 'd', 'e', 'f'],
         'd' : ['b', 'c', 'e'],
         'e' : ['a', 'c', 'd'],
         'f' : ['c']}

    G =nx.Graph(graph)
    nx.draw(G, with_labels = True)
    bfs(graph, 'a')           
    dfs(graph, 'a')

if  __name__ == '__main__':
    main()