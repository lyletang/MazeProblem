# Describe: Search a maze using a queue (recording the path precedent relation)
# Author: Jiahui Tang
# Date: 2017-1-3

# import the necessary package
from mazeMap import *
from SQueue import *

def build_path(start, pos, end, precedent):
    path = [end]
    while pos != start:
        path.append(pos)
        pos = precedent[pos]
    path.append(start)
    path.reverse()
    return path    

def maze_solver_queue_withpath(maze, start, end):
    if start == end:
        return [start]
    qu = SQueue()
    precedent = dict()
    mark(maze, start)                
    qu.enqueue(start)        # start position into queue
    while not qu.is_empty(): # have possibility to try
        pos = qu.dequeue()   # take next try position
        for i in range(4):   # chech each direction
            nextp = (pos[0] + dirs[i][0],
                     pos[1] + dirs[i][1]) # next position
            if passable(maze, nextp):     # find new position
                if nextp == end:         # find end, great!
                    return build_path(start, pos, end, precedent)
                mark(maze, nextp)
                precedent[nextp] = pos    # set precedent of nextp
                qu.enqueue(nextp)         # new position into queue
    print("No path.")  # no path
# end maze_solver_queue (record the path)

if __name__ == '__main__':
    pass
