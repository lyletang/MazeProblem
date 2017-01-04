# Describe: A maze path finder which use a stack storage
# Author: Jiahui Tang
# Date: 2017-1-3

# import the necessary package
from mazeMap import *
from SStack import *

def print_path(end, last, st):
    print(end, last, sep=" ", end=' ')
    while not st.is_empty():
        print(st.pop()[0], end=' ')
    print('\n')

def print_path_rev(end, last, st): # print the path from start to end
    path = [end, last]
    while not st.is_empty():
        path.append(st.pop())
    path.reverse()
    for pos in path:
        print(pos, end = " ")
    print('\n')

def maze_solver_stack(maze, start, end):
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze, start)                 
    st.push((start, 0))         # start position into stack
    while not st.is_empty():    # have possibility to try
        pos, nxt = st.pop()     # get last branch position
        for i in range(nxt, 4): # try to find unexploring dir(s)
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1]) # next point
            if nextp == end:        # find end, great!
                print_path(end, pos, st)
                return
            if passable(maze, nextp):# new position is passable
                st.push((pos, i+1))  # original position in stack
                mark(maze, nextp)
                st.push((nextp, 0))  # new position into stack
                break
    print("No path.")  # no path
# end maze_solver_stack

if __name__ == '__main__':
    pass
