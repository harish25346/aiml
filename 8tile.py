import heapq 
n = 3 
directions = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]  
class Node: 
    def __init__(self, parent, mat, empty_tile_pos, cost, move=''): 
        self.parent = parent 
        self.mat = mat   
        self.empty_tile_pos = empty_tile_pos 
        self.cost = cost   
        self.move = move  
    def __lt__(self, other): 
        return self.cost < other.cost   
def calculate_cost(mat, goal): 
    """Returns the number of misplaced tiles.""" 
    return sum(mat[i][j] != goal[i][j] and mat[i][j] != 0 for i in range(n) for j in range(n)) 
def create_new_node(parent, mat, empty_tile_pos, new_tile_pos, goal, move): 
    """Creates a new node by swapping the empty tile.""" 
    x1, y1 = empty_tile_pos 
    x2, y2 = new_tile_pos 
    new_mat = [row[:] for row in mat]  
    new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1] 
    return Node(parent, new_mat, new_tile_pos, calculate_cost(new_mat, goal), move) 
def print_matrix(mat): 
    """Prints the matrix in a readable format.""" 
    for row in mat: 
        print(" ".join(map(str, row))) 
    print() 
def print_solution(node): 
    """Prints the solution path from start to goal, including moves.""" 
    path = [] 
    while node: 
        path.append(node) 
        node = node.parent 
    for step in reversed(path): 
        if step.move:  
            print(f"Move: {step.move}") 
        print_matrix(step.mat) 
def solve(initial, empty_tile_pos, goal): 
    """Solves the 8-puzzle problem using Best-First Search.""" 
    open_list = [] 
    visited = set() 
    root = Node(None, initial, empty_tile_pos, calculate_cost(initial, goal)) 
    heapq.heappush(open_list, root) 
    visited.add(tuple(map(tuple, root.mat)))  
    while open_list: 
        node = heapq.heappop(open_list) 
 
        if node.cost == 0:  
            print_solution(node) 
            return 
 
        x, y = node.empty_tile_pos 
        for dx, dy, move in directions: 
            new_x, new_y = x + dx, y + dy 
 
            if 0 <= new_x < n and 0 <= new_y < n: 
                child = create_new_node(node, node.mat, (x, y), (new_x, new_y), goal, move) 
                if tuple(map(tuple, child.mat)) not in visited:  
                    heapq.heappush(open_list, child) 
                    visited.add(tuple(map(tuple, child.mat))) 
initial = [[1, 2, 3], [5, 6, 0], [7, 8, 4]] 
goal = [[1, 2, 3], [0, 8, 6], [5, 7, 4]] 
empty_tile_pos = (1, 2)   
solve(initial, empty_tile_pos, goal)