# for 120x120 maze generation
import numpy as np

'''
layout1 =   [[1,1,1,1,1,1,1,1,1,1],
            [1,0,1,0,1,0,1,0,0,1],
            [1,0,1,0,0,0,1,0,1,1],
            [1,0,0,0,1,1,1,2,0,1],
            [1,0,1,0,0,0,0,0,1,1],
            [1,0,1,0,1,1,1,0,1,1],
            [1,0,1,0,1,0,0,0,1,1],
            [1,0,1,0,1,1,1,0,1,1],
            [1,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1]]
layout2 =   [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1,0,1],
            [1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1],
            [1,0,0,0,1,1,1,2,0,1,0,1,0,0,1,1,0,1,0,1],
            [1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
            [1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
            [1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1],
            [1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
'''
# array_maze = np.load('C:/Users/Etoile/Desktop/labyrinth/Marble-Maze_test/array_label.npy')
# layout = array_maze.tolist()
# print(layout)

#from gameObjects import check_layout
class check_layout:
    '''
    this is our viewpoint in the game. Please use check_layout.print_layout()
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1], 
    [1, 0, 1, 0, 1, 0, 0, 0, 1, 1], 
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1], 
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 1], 
    [1, 0, 0, 0, 1, 1, 1, 2, 0, 1], 
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 1], 
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    '''
    def __init__(self, layout=layout):
        self.origin_view = layout
        new_layout = []
        for i in range(len(layout[:][0])):
            new_layout.append([])
            idx = len(layout[0][:])-1-i
            for j in range(len(layout[0][:])):
                new_layout[i].append(layout[idx][j])
            
        self.new_layout = new_layout
        # print(len(layout[0][:]))
        # print(len(layout[:][1]))
        
    def print_layout(self, flip = 1):
        if flip == 1:
            for i in range(len(self.new_layout[0][:])):
                print(self.new_layout[:][i])
        else:
            for i in range(len(self.origin_view[0][:])):
                print(self.origin_view[:][i])

size = 480
new_layout = []
for row in range(size):
    new_layout.append([])
    for col in range(size):
        if (row == 0) or (row == size-1):
            new_layout[row].append(1)
        elif (col == size-1) or (col == 0):
            new_layout[row].append(1)
        else: new_layout[row].append(0)

# for row in range(size):
#     for col in range(size):
#         if (row == 0 or row == size) or (col == 0 or col == size):
#             new_layout[row][col] = 1
#         else: new_layout[row][col] = 0
print(new_layout)

f = open("./layout.txt", 'w')
for row in range(size):
    for col in range(size):
        f.write(str(new_layout[row][col]))
    f.write("\n")
f.close()