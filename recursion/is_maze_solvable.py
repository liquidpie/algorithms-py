def is_maze_solvable(maze, n):
    """
        checks if the maze is solvable from starting point marked by 'S'
         to the finishing point marked by 'E'
         
         '*' indicates the walls of maze
         ' ' indicates free path
        
    :param maze: maze to be solved
    :param n: size of maze
    :return: True if maze is solvable, otherwise False
    
    """

    start_x = -1
    start_y = -1

    # look through grid to find our starting point
    (start_x, start_y) = [(x, y) for x in range(0, n) for y in range(0, n) if maze[x][y] == 'S'][0]

    # if starting point is not found, maze is not solvable
    if start_x == -1 or start_y == -1:
        return False

    return solve_maze(maze, n, start_x, start_y)


def solve_maze(maze, n, x, y):

    # if the current position is off grid, maze isn't solvable
    if x >= n or x < 0 or y >= n or y < 0:
        return False

    # if current position is '*', we can't continue this path
    if maze[x][y] == "*":
        return False

    # if current position is 'E', then we are at the end and maze is solvable
    if maze[x][y] == "E":
        return True

    # if the current position is visited, return False to prevent cycles
    if maze[x][y] == "-":
        return False

    # mark the current position as visited by filling in '-'
    maze[x][y] = "-"

    # otherwise, keep exploring by trying each possible next step from this
    # point. If any of the options solve the maze, return True
    if solve_maze(maze, n, x - 1, y):
        return True
    if solve_maze(maze, n, x + 1, y):
        return True
    if solve_maze(maze, n, x, y - 1):
        return True
    if solve_maze(maze, n, x, y + 1):
        return True

    # if none of the possibilities could solve the maze, return False
    return False

if __name__ == '__main__':
    maze = list(list())
    maze.append(['*', '*', '*', '*', '*', ' ', ' ', ' '])
    maze.append(['*', ' ', ' ', ' ', '*', ' ', ' ', ' '])
    maze.append(['*', 'S', '*', '*', '*', ' ', ' ', ' '])
    maze.append(['*', ' ', ' ', ' ', '*', '*', '*', '*'])
    maze.append(['*', ' ', '*', ' ', ' ', ' ', ' ', '*'])
    maze.append(['*', ' ', ' ', ' ', '*', ' ', ' ', '*'])
    maze.append(['*', '*', '*', '*', '*', ' ', 'E', '*'])
    maze.append([' ', ' ', ' ', ' ', '*', '*', '*', '*'])

    print("Is maze solvable:", is_maze_solvable(maze, len(maze)))

