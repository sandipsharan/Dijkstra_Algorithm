import numpy as np
import copy
from matplotlib import pyplot as plt
from queue import PriorityQueue
import time
start_time = time.time()


queue_nodes = PriorityQueue()
path_dict = {}
visited_nodes = []
best_path = []
index = 0

def map_plot():
    fig = plt.figure()
    fig.set_dpi(100)
    fig.set_size_inches(24, 10)
    ax = plt.axes(xlim=(0, 600), ylim=(0, 250))
    obstacles = []
    clearance_x = []
    clearance_y = []
    original_x = []
    original_y = []
    walls_x = []
    walls_y = []
    for x in range (0,601, 1):
        for y in range(0, 251, 1):
            if  (95 <= x <= 155) and (0 <= y <= 105):
                obstacles.append((x,y))
                clearance_x.append(x)
                clearance_y.append(y)
            if  (95 <= x <= 155) and (145 <= y <= 250):
                obstacles.append((x,y))
                clearance_x.append(x)
                clearance_y.append(y)
            if  (y +2*x - 1156) < 0 and (y- 2*x + 906) > 0 and (455 <= x):
                obstacles.append((x,y))
                clearance_x.append(x)
                clearance_y.append(y)
            if  (y - (15/26)*x - (425/13)) < 0 and (y + (15/26)*x - (4925/13)) < 0 and (y - (15/26)*x + (1675/13)) > 0 and (y + (15/26)*x - (2825/13)) > 0 and (230 <= x <= 370):
                obstacles.append((x,y))
                clearance_x.append(x)
                clearance_y.append(y)
            
            if  (100 <= x <= 150) and (0 <= y <= 100):
                obstacles.append((x,y))
                original_x.append(x)
                original_y.append(y)
            if  (100 <= x <= 150) and (150 <= y <= 250):
                obstacles.append((x,y))
                original_x.append(x)
                original_y.append(y)
            if  (y +2*x - 1145) < 0 and (y- 2*x + 895) > 0 and (460 <= x):
                obstacles.append((x,y))
                original_x.append(x)
                original_y.append(y)
            if  (y - (15/26)*x - (350/13)) < 0 and (y + (15/26)*x - (4850/13)) < 0 and (y - (15/26)*x + (1600/13)) > 0 and (y + (15/26)*x - (2900/13)) > 0 and (235 <= x <= 365):
                obstacles.append((x,y))
                original_x.append(x)
                original_y.append(y)
            if (0 <= x <= 5) or (0 < y < 5) or (595 <= x <= 600) or (245 <= y <=250):
                obstacles.append((x,y))
                walls_x.append(x)
                walls_y.append(y)
    ax.set_facecolor("black")
    ax.scatter(clearance_x, clearance_y, color = 'teal', marker = 'o')
    ax.scatter(original_x, original_y, color = 'turquoise', marker = 'o')
    ax.scatter(walls_x, walls_y, color = 'teal', marker = 'o')
    
    return obstacles

# To get initial state from the user
def input_initial_state():
    input_node = input('Enter the initial state : ')
    input_node = tuple(int(i) for i in input_node.split(" "))
    print(input_node)
    if input_node in obstacle_space:
        print('The given node is in obstacle space')
        input_initial_state()
    if input_node[0] > 600 or input_node[1] > 250:
        print('The input node is not in the limits')
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
    if goal_node[0] > 600 or goal_node[1] > 250:
        print('The goal node is not in the limits')
        input_goal_state()
    return goal_node

# To move up
def ActionMoveUp(pos, queue, goal):
    global index
    if queue != goal: 
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
def ActionMoveDown(pos, queue, goal):
    global index
    if queue != goal:
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
def ActionMoveRight(pos, queue, goal):
    global index
    if queue != goal:
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
def ActionMoveLeft(pos, queue, goal):
    global index
    if queue != goal:
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
def ActionMoveUpRight(pos, queue, goal):
    global index
    if queue != goal:
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
def ActionMoveUpLeft(pos, queue, goal):
    global index
    if queue != goal:
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
def ActionMoveDownRight(pos, queue, goal):
    global index
    if queue != goal:
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
def ActionMoveDownLeft(pos, queue, goal):
    global index
    if queue != goal:
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


obstacle_space = map_plot()

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
            ActionMoveUp(position,queue_pop, node_state_g)
        if y-1 >= 0:
            ActionMoveDown(position,queue_pop, node_state_g)
        if x+1 <= 600:
            ActionMoveRight(position,queue_pop, node_state_g)
        if x-1 >= 0:
            ActionMoveLeft(position,queue_pop, node_state_g)
        if (x+1) <= 600 and (y+1) <= 250:
            ActionMoveUpRight(position,queue_pop, node_state_g)
        if (x-1) >= 0 and (y+1) <= 250:
            ActionMoveUpLeft(position,queue_pop, node_state_g)
        if (x+1) <= 600 and (y-1) >= 0:
            ActionMoveDownRight(position,queue_pop, node_state_g)
        if (x-1) >= 0 and (y-1) >= 0:
            ActionMoveDownLeft(position,queue_pop, node_state_g)
    else:
        print("Goal Reached: ", node_state_g)
        break
plt.show()
end_time = time.time()

# get the execution time
elapsed_time = end_time - start_time
print('Execution time:', elapsed_time, 'seconds')
