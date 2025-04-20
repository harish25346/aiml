def is_consistent(assignment, var, val, adjacency_list): 
    for neighbor in adjacency_list[var]: 
        if neighbor in assignment and assignment[neighbor] == val: 
            return False 
    return True 
 
def select_unassigned_variable(variables, assignment): 
    for var in variables: 
        if var not in assignment: 
            return var 
    return None 
def backtracking(assignment, variables, domains, adjacency_list): 
    if len(assignment) == len(variables): 
        return assignment   
    var = select_unassigned_variable(variables, assignment) 
    for val in domains[var]: 
        if is_consistent(assignment, var, val, adjacency_list): 
            assignment[var] = val  
            result = backtracking(assignment, variables, domains, adjacency_list) 
            if result: 
                return result  
            assignment.pop(var)   
    return None  
if __name__ == "__main__": 
    variables = ['WA', 'NT', 'SA', 'QLD', 'NSW', 'VIC', 'TAS'] 
    domains = {var: ['Red', 'Green', 'Blue'] for var in variables} 
    adjacency_list = { 
        'WA': ['NT', 'SA'], 
        'NT': ['WA', 'SA', 'QLD'], 
        'SA': ['WA', 'NT', 'QLD', 'NSW', 'VIC'], 
        'QLD': ['NT', 'SA', 'NSW'], 
        'NSW': ['SA', 'QLD', 'VIC'], 
        'VIC': ['SA', 'NSW'], 
        'TAS': []   
    } 
    assignment = {} 
    solution = backtracking(assignment, variables, domains, adjacency_list) 
    if solution: 
        print("Solution:", solution) 
    else: 
        print("No Solution Found")