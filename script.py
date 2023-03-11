import numpy as np
import copy
from matplotlib import pyplot as plt
from queue import PriorityQueue


queue_nodes = PriorityQueue()
path_dict = {}
visited_nodes = []
best_path = []
index = 0

def map_plot():
    fig = plt.figure()
    fig.set_dpi(100)
    fig.set_size_inches(24, 10)
    ac = plt.axes(xlim=(0, 600), ylim=(0, 250))
    obstacles = []
    for x in range (0,601, 1):
        for y in range(0, 251, 1):
            if  (95 <= x <= 155) and (0 <= y <= 105):
                obstacles.append((x,y))
                # ax.plot(x,y, color = 'red', marker='o', markersize=5)
            if  (95 <= x <= 155) and (145 <= y <= 250):
                obstacles.append((x,y))
                # ax.plot(x,y, color = 'red', marker='o', markersize=5)
            if  (y +2*x - 1156) < 0 and (y- 2*x + 906) > 0 and (460 <= x):
                # ax.plot(x,y, color = 'red', marker='o', markersize=5)
                obstacles.append((x,y))
            if  (y - (15/26)*x - (425/13)) < 0 and (y + (15/26)*x - (4925/13)) < 0 and (y - (15/26)*x + (1675/13)) > 0 and (y + (15/26)*x - (2825/13)) > 0 and (230 <= x <= 370):
                # ax.plot(x,y, color = 'red', marker='o', markersize=5)
                obstacles.append((x,y))
    # plt.show()
    
    return ac, obstacles

# To get initial state from the user
def input_initial_state():
    input_node = input('Enter the initial state : ')
    input_node = tuple(int(i) for i in input_node.split(" "))
    print(input_node)
    if input_node in obstacle_space:
        print('The given node is in obstacle space')
        input_initial_state()
    return input_node

# To get goal state from the user
def input_goal_state():
    goal_node = input('Enter the goal state : ')
    goal_node = tuple(int(j) for j in goal_node.split(" "))
    print(goal_node)
    if goal_node in obstacle_space:
        print('The given node is in obstacle space')
        input_goal_state()
    return goal_node

# To move up
def ActionMoveUp(pos, queue):
    global index
    node_position = pos
    current_position = (pos[0], pos[1]+1)
    cost2_come = queue[0] +1
    index += 1
    parent_node = queue[1]
    node = (cost2_come, index, parent_node, current_position)
    if current_position not in visited_nodes and obstacle_space:
        for i in range(queue_nodes.qsize()):
            if queue_nodes.queue[i][3] == current_position:
                if queue_nodes.queue[i][0] > cost2_come:
                    index += 1
                    queue_nodes.queue[i] = (cost2_come, index, parent_node, current_position)
                    path_dict[queue_nodes.queue[i][3]] = node_position
                    return
                else:
                    return
        queue_nodes.put(node)
        queue_parent = node_position
        queue_child = current_position
        path_dict[queue_child] = queue_parent
    return 

# To move down
def ActionMoveDown(pos, queue):
    global index
    node_position = pos
    current_position = (pos[0], pos[1]-1)
    cost2_come = queue[0] +1
    index += 1
    parent_node = queue[1]
    node = (cost2_come, index, parent_node, current_position)
    if current_position not in visited_nodes and obstacle_space:
        for i in range(queue_nodes.qsize()):
            if queue_nodes.queue[i][3] == current_position:
                if queue_nodes.queue[i][0] > cost2_come:
                    index += 1
                    queue_nodes.queue[i] = (cost2_come, index, parent_node, current_position)
                    path_dict[queue_nodes.queue[i][3]] = node_position
                    return
                else:
                    return
        queue_nodes.put(node)
        queue_parent = node_position
        queue_child = current_position
        path_dict[queue_child] = queue_parent
    return 

# To move right
def ActionMoveRight(pos, queue):
    global index
    node_position = pos
    current_position = (pos[0]+1, pos[1])
    cost2_come = queue[0] +1
    index += 1
    parent_node = queue[1]
    node = (cost2_come, index, parent_node, current_position)
    if current_position not in visited_nodes and obstacle_space:
        for i in range(queue_nodes.qsize()):
            if queue_nodes.queue[i][3] == current_position:
                if queue_nodes.queue[i][0] > cost2_come:
                    index += 1
                    queue_nodes.queue[i] = (cost2_come, index, parent_node, current_position)
                    path_dict[queue_nodes.queue[i][3]] = node_position
                    return
                else:
                    return
        queue_nodes.put(node)
        queue_parent = node_position
        queue_child = current_position
        path_dict[queue_child] = queue_parent
    return 

# To move left
def ActionMoveLeft(pos, queue):
    global index
    node_position = pos
    current_position = (pos[0]-1, pos[1])
    cost2_come = queue[0] +1
    index += 1
    parent_node = queue[1]
    node = (cost2_come, index, parent_node, current_position)
    if current_position not in visited_nodes and obstacle_space:
        for i in range(queue_nodes.qsize()):
            if queue_nodes.queue[i][3] == current_position:
                if queue_nodes.queue[i][0] > cost2_come:
                    index += 1
                    queue_nodes.queue[i] = (cost2_come, index, parent_node, current_position)
                    path_dict[current_position] = node_position
                    return
                else:
                    return
        queue_nodes.put(node)
        queue_parent = node_position
        queue_child = current_position
        path_dict[queue_child] = queue_parent
    return 

# To move up and right diagonally
def ActionMoveUpRight(pos, queue):
    global index
    node_position = pos
    current_position = (pos[0]+1, pos[1]+1)
    cost2_come = queue[0] + 1.4
    index += 1
    parent_node = queue[1]
    node = (cost2_come, index, parent_node, current_position)
    if current_position not in visited_nodes and obstacle_space:
        for i in range(queue_nodes.qsize()):
            if queue_nodes.queue[i][3] == current_position:
                if queue_nodes.queue[i][0] > cost2_come:
                    index += 1
                    queue_nodes.queue[i] = (cost2_come, index, parent_node, current_position)
                    path_dict[queue_nodes.queue[i][3]] = node_position
                    return
                else:
                    return
        queue_nodes.put(node)
        queue_parent = node_position
        queue_child = current_position
        path_dict[queue_child] = queue_parent
    return 

# To move up and left diagonally
def ActionMoveUpLeft(pos, queue):
    global index
    node_position = pos
    current_position = (pos[0]-1, pos[1]+1)
    cost2_come = queue[0] + 1.4
    index += 1
    parent_node = queue[1]
    node = (cost2_come, index, parent_node, current_position)
    if current_position not in visited_nodes and obstacle_space:
        for i in range(queue_nodes.qsize()):
            if queue_nodes.queue[i][3] == current_position:
                if queue_nodes.queue[i][0] > cost2_come:
                    index += 1
                    queue_nodes.queue[i] = (cost2_come, index, parent_node, current_position)
                    path_dict[queue_nodes.queue[i][3]] = node_position
                    return
                else:
                    return
        queue_nodes.put(node)
        queue_parent = node_position
        queue_child = current_position
        path_dict[queue_child] = queue_parent
    return 

# To move down and right diagonally
def ActionMoveDownRight(pos, queue):
    global index
    node_position = pos
    current_position = (pos[0]+1, pos[1]-1)
    cost2_come = queue[0] + 1.4
    index += 1
    parent_node = queue[1]
    node = (cost2_come, index, parent_node, current_position)
    if current_position not in visited_nodes and obstacle_space:
        for i in range(queue_nodes.qsize()):
            if queue_nodes.queue[i][3] == current_position:
                if queue_nodes.queue[i][0] > cost2_come:
                    index += 1
                    queue_nodes.queue[i] = (cost2_come, index, parent_node, current_position)
                    path_dict[queue_nodes.queue[i][3]] = node_position
                    return
                else:
                    return
        queue_nodes.put(node)
        queue_parent = node_position
        queue_child = current_position
        path_dict[queue_child] = queue_parent
    return 


# To move down and left diagonally
def ActionMoveDownLeft(pos, queue):
    global index
    node_position = pos
    current_position = (pos[0]-1, pos[1]-1)
    cost2_come = queue[0] + 1.4
    index += 1
    parent_node = queue[1]
    node = (cost2_come, index, parent_node, current_position)
    if current_position not in visited_nodes and obstacle_space:
        for i in range(queue_nodes.qsize()):
            if queue_nodes.queue[i][3] == current_position:
                if queue_nodes.queue[i][0] > cost2_come:
                    index += 1
                    queue_nodes.queue[i] = (cost2_come, index, parent_node, current_position)
                    path_dict[queue_nodes.queue[i][3]] = node_position
                    return
                else:
                    return
        queue_nodes.put(node)
        queue_parent = node_position
        queue_child = current_position
        path_dict[queue_child] = queue_parent
    return 


ax, obstacle_space = map_plot()
for i in obstacle_space:
    ax.scatter(int(i[0]), int(i[1]), color = 'b', marker='o')
    plt.show()
initial_input = input_initial_state()
node_state_i = (0, 0, 0, (initial_input))
node_state_g = input_goal_state()
queue_nodes.put(node_state_i)

while True:
    queue_pop = queue_nodes.get(0)
    visited_nodes.append(queue_pop[3])
    position = queue_pop[3]
    x, y = position
    if position != node_state_g:
        if y+1 <= 250:
            ActionMoveUp(position,queue_pop)
        if y-1 >= 0:
            ActionMoveDown(position,queue_pop)
        if x+1 <= 600:
            ActionMoveRight(position,queue_pop)
        if x-1 >= 0:
            ActionMoveLeft(position,queue_pop)
        if (x+1) <= 600 and (y+1) <= 250:
            ActionMoveUpRight(position,queue_pop)
        if (x-1) >= 0 and (y+1) <= 250:
            ActionMoveUpLeft(position,queue_pop)
        if (x+1) <= 600 and (y-1) >= 0:
            ActionMoveDownRight(position,queue_pop)
        if (x-1) >= 0 and (y-1) >= 0:
            ActionMoveDownLeft(position,queue_pop)
    else:
        print("Fuck you")
        # pass
        break
