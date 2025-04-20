def is_consistent(assignment, row, col):
    for r, c in assignment.items():
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True

def select_unassigned_variable(variables, assignment):
    for row in variables:
        if row not in assignment:
            return row
    return None

def backtracking(assignment, variables, domains):
    if len(assignment) == len(variables):
        return assignment

    row = select_unassigned_variable(variables, assignment)

    for col in domains:
        if is_consistent(assignment, row, col):
            assignment[row] = col
            result = backtracking(assignment, variables, domains)
            if result:
                return result
            assignment.pop(row)

    return None

if __name__ == "__main__":
    n = int(input("Enter the size of the board (n): "))
    variables = list(range(n))
    domains = list(range(n))
    assignment = {}

    solution = backtracking(assignment, variables, domains)

    if solution:
        print("Solution:")
        for row in range(n):
            board_row = ['Q' if solution.get(row) == col else '.' for col in range(n)]
            print(' '.join(board_row))
    else:
        print("No Solution Found")
