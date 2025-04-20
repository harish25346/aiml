import heapq 
class Node: 
    def __init__(self, x, y, g, h): 
        self.x = x   
        self.y = y   
        self.g = g  
        self.h = h   
        self.f = g + h 
        self.parent = None    
    def __lt__(self, other): 
        return self.f < other.f   
def heuristic(x, y, target_x, target_y): 
    return abs(x - target_x) + abs(y - target_y)  
def a_star_water_jug(capacity_x, capacity_y, target_x, target_y): 
    open_list = [] 
    visited = set() 
    solutions = [] 
    start_node = Node(0, 0, 0, heuristic(0, 0, target_x, target_y)) 
    heapq.heappush(open_list, start_node)     
    while open_list: 
        current = heapq.heappop(open_list)       
        if (current.x, current.y) == (target_x, target_y): 
            path = [] 
            while current: 
                path.append((current.x, current.y)) 
                current = current.parent 
            solutions.append(path[::-1]) 
            continue  

        if (current.x, current.y) in visited: 
            continue         
        visited.add((current.x, current.y)) 
        moves = [ 
            (capacity_x, current.y),   
            (current.x, capacity_y),   
            (0, current.y),            
            (current.x, 0),            
            (current.x - min(current.x, capacity_y - current.y), current.y + min(current.x, 
capacity_y - current.y)), 
            (current.x + min(current.y, capacity_x - current.x), current.y - min(current.y, capacity_x - current.x))    
        ]      
        for new_x, new_y in moves: 
            if (new_x, new_y) not in visited: 
                new_node = Node(new_x, new_y, current.g + 1, heuristic(new_x, new_y, target_x, 
target_y)) 
                new_node.parent = current 
                heapq.heappush(open_list, new_node) 

    return solutions  
capacity_x = 4 
capacity_y = 3 
target_x = 2 
target_y = 0 

solutions = a_star_water_jug(capacity_x, capacity_y, target_x, target_y) 
for solution in solutions: 
  for step in solution: 
    print(step) 
print("Solution found")