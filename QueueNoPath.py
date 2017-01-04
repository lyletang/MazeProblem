# Describe: Search a maze using a queue (No path record)
# Author: Jiahui Tang
# Date: 2017-1-3

# import the necessary package
from mazeMap import *
from SQueue import *

def maze_solver_queue_nopath(maze, start, end):
    if start == end:
        print("Path finds.")
        return
    qu = SQueue()
    mark(maze, start)                
    qu.enqueue(start)        # start position into queue
    while not qu.is_empty(): # have possibility to try
        pos = qu.dequeue()   # take next try position
        for i in range(4):   # chech each direction
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1]) # next position
            if passable(maze, nextp):     # find new position
                if nextp == end:          # find end, great!
                    print("Path finds.")
                    return
                mark(maze, nextp)
                qu.enqueue(nextp)         # new position into queue
    print("No path.")  # no path
# end maze_solver_queue (no path record)

if __name__ == 'main':	
    pass
