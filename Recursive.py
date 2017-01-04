# Describe: A recursive maze path finder
# Author: Jiahui Tang
# Date: 2017-1-3

# import the necessary package
from mazeMap import *

def maze_solver_rec(maze, start, end):
    """ 
	A maze solver using a recursive procedure to find the path.
    """
    def find_path(maze, start, end):
        mark(maze, start);
        if start == end:
            print(start, end=' ')
            return True
        for i in range(4):
            nextp = start[0]+dirs[i][0], start[1]+dirs[i][1]
            if passable(maze, nextp):
                if find_path(maze, nextp, end):
                    print(start, end=' ')
                    return True;
        return False

    print("If find, print the path from end to start:")
    if find_path(maze, start, end):
        print("\n")
    else:
        print("No path exists.")
# end maze_solver_rec

if __name__ == '__main__':
    pass
