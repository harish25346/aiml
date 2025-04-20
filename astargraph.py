import heapq  
class Node:  
    def __init__(self, name, g, h):  
        self.name = name      
        self.g = g           
        self.h = h            
        self.f = g + h        
        self.parent = None          
    def __lt__(self, other):    
        return self.f < other.f   
def a_star(graph, heuristics, start, goal):  
    open_list = []  
    closed_set = set()       
    start_node = Node(start, 0, heuristics[start])  
    heapq.heappush(open_list, start_node)       
    while open_list:  
        current_node = heapq.heappop(open_list)        
        if current_node.name == goal:    
            path = []  
            while current_node:  
                path.append(current_node.name)  
                current_node = current_node.parent  
            return path[::-1]       
        closed_set.add(current_node.name)    
        for neighbor, cost in graph[current_node.name].items():  
            if neighbor in closed_set:  
                continue    
            g_cost = current_node.g + cost  # New cost  
            h_cost = heuristics[neighbor]  # Estimated heuristic cost  
            neighbor_node = Node(neighbor, g_cost, h_cost)  
            neighbor_node.parent = current_node  # Store path  
            heapq.heappush(open_list, neighbor_node)  
    return None  
graph = {  
    'A': {'B': 1, 'C': 4},  
    'B': {'A': 1, 'D': 2},  
    'C': {'A': 4, 'E': 5},  
    'D': {'B': 2, 'E': 1},  
    'E': {'C': 5, 'D': 1, 'F': 3, 'G': 2},  
    'F': {'E': 3},  
    'G': {'E': 2}  
}  
heuristics = {  
    'A': 6, 'B': 5, 'C': 4, 'D': 3,  
    'E': 2, 'F': 3, 'G': 0  
} 
start_node = 'A'  
goal_node = 'G'  
path = a_star(graph, heuristics, start_node, goal_node)  
print("Shortest path:", path) 