from queue import PriorityQueue
import time
import vidmaker
import pygame


start_time = time.time()
queue_nodes = PriorityQueue()
path_dict = {}
visited_nodes = []
best_path = []
index = 0


# To convert the coordinates from top-left corner to bottom-left
def flip_coords(points, h):
    return (points[0], h - points[1])

# To convert the coordinates from top-left corner to bottom-left
def flip_coords_rect(points, h, obj_h):
    return (points[0], h - points[1] - obj_h)

# Function for    
def game(explored, optimal_path):
    pygame.init()
    surface = pygame.display.set_mode((600,250))
    color_1 = "skyblue"
    color_2 = "teal"
    running = True
    # video = vidmaker.Video("Path_planner.mp4", late_export=True)
    clock = pygame.time.Clock()


    clearance_rect_down = flip_coords_rect([95, 0], 250, 105)
    clearance_rect_up = flip_coords_rect([95, 145], 250, 105)
    original_rect_down = flip_coords_rect([100, 0], 250, 100)
    original_rect_up = flip_coords_rect([100, 150], 250, 100)

    clearance_triangle_1 = flip_coords([455, 20], 250)
    clearance_triangle_2 = flip_coords([463, 20], 250)
    clearance_triangle_3 = flip_coords([515.5, 125], 250)
    clearance_triangle_4 = flip_coords([463, 230], 250)
    clearance_triangle_5 = flip_coords([455, 230], 250)

    original_triangle_1 = flip_coords([460, 25], 250)
    original_triangle_2 = flip_coords([460, 225], 250)
    original_triangle_3 = flip_coords([510, 125], 250)

    clearance_hexagon_1 = flip_coords([300, 205.76], 250)
    clearance_hexagon_2 = flip_coords([230, 165.38], 250)
    clearance_hexagon_3 = flip_coords([230, 84.61], 250)
    clearance_hexagon_4 = flip_coords([300, 44.23], 250)
    clearance_hexagon_5 = flip_coords([370, 84.61], 250)
    clearance_hexagon_6 = flip_coords([370, 165.38], 250)

    original_hexagon_1 = flip_coords([235,87.5], 250)
    original_hexagon_2 = flip_coords([300,50], 250)
    original_hexagon_3 = flip_coords([365,87.5], 250)
    original_hexagon_4 = flip_coords([365,162.5], 250)
    original_hexagon_5 = flip_coords([300,200], 250)
    original_hexagon_6 = flip_coords([235,162.5], 250)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.draw.rect(surface, color_2, pygame.Rect(clearance_rect_down[0], clearance_rect_down[1], 60, 105))
        pygame.draw.rect(surface, color_2, pygame.Rect(clearance_rect_up[0], clearance_rect_up[1], 60, 105))
        pygame.draw.rect(surface, color_1, pygame.Rect(original_rect_down[0], original_rect_down[1], 50, 100))
        pygame.draw.rect(surface, color_1, pygame.Rect(original_rect_up[0], original_rect_up[1], 50, 100))

        pygame.draw.polygon(surface, color_2, ((clearance_triangle_1),(clearance_triangle_2),(clearance_triangle_3), (clearance_triangle_4), (clearance_triangle_5)))
        pygame.draw.polygon(surface, color_1, ((original_triangle_1),(original_triangle_2),(original_triangle_3)))

        pygame.draw.polygon(surface, color_2, ((clearance_hexagon_1),(clearance_hexagon_2),(clearance_hexagon_3),(clearance_hexagon_4),(clearance_hexagon_5),(clearance_hexagon_6)))
        pygame.draw.polygon(surface, color_1, ((original_hexagon_1),(original_hexagon_2),(original_hexagon_3),(original_hexagon_4),(original_hexagon_5),(original_hexagon_6)))

        pygame.draw.rect(surface, color_2 ,pygame.Rect(0, 0, 600, 5))
        pygame.draw.rect(surface, color_2 ,pygame.Rect(0, 245, 600, 5))
        pygame.draw.rect(surface, color_2 ,pygame.Rect(0, 0, 5, 250))
        pygame.draw.rect(surface, color_2 ,pygame.Rect(595, 0, 5, 250))

        for j in explored:
            pygame.draw.circle(surface, "lightcyan", flip_coords(j, 250), 1)
            # video.update(pygame.surfarray.pixels3d(surface).swapaxes(0, 1), inverted=False)
            pygame.display.flip()
            clock.tick(700)

        for i in optimal_path:
            pygame.draw.circle(surface, "darkslategray", flip_coords(i, 250), 1)
            # video.update(pygame.surfarray.pixels3d(surface).swapaxes(0, 1), inverted=False)
            pygame.display.flip()
            clock.tick(10)
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False
    pygame.quit()
    # video.export(verbose=True)


def map_plot():
    obstacle = []
    for x in range (0,601, 1):
        for y in range(0, 251, 1):
            if  (95 <= x <= 155) and (0 <= y <= 105):
                obstacle.append((x,y))
            if  (95 <= x <= 155) and (145 <= y <= 250):
                obstacle.append((x,y))
            if  (y +2*x - 1156) < 0 and (y- 2*x + 906) > 0 and (455 <= x) and (20 <= y <= 230):
                obstacle.append((x,y))
            if  (y - (15/26)*x - (425/13)) < 0 and (y + (15/26)*x - (4925/13)) < 0 and (y - (15/26)*x + (1675/13)) > 0 and (y + (15/26)*x - (2825/13)) > 0 and (230 <= x <= 370):
                obstacle.append((x,y))
            if  (100 <= x <= 150) and (0 <= y <= 100):
                obstacle.append((x,y))
            if  (100 <= x <= 150) and (150 <= y <= 250):
                obstacle.append((x,y))
            if  (y +2*x - 1145) < 0 and (y- 2*x + 895) > 0 and (460 <= x) and (20 <= y <= 230):
                obstacle.append((x,y))
            if  (y - (15/26)*x - (350/13)) < 0 and (y + (15/26)*x - (4850/13)) < 0 and (y - (15/26)*x + (1600/13)) > 0 and (y + (15/26)*x - (2900/13)) > 0 and (235 <= x <= 365):
                obstacle.append((x,y))
            if (0 <= x <= 5) or (0 <= y <= 5) or (595 <= x <= 600) or (245 <= y <=250):
                obstacle.append((x,y))
    
    return obstacle

# To get initial state from the user
def input_initial_state():
    input_node = input('Enter the initial state with space : ')
    input_node = tuple(int(i) for i in input_node.split(" "))
    print(input_node)
    if input_node in obstacle_space:
        print('The given node is in obstacle space')
        input_initial_state()
    if input_node[0] > 600 or input_node[1] > 250 or input_node[0] < 0 or input_node[1] < 0:
        print('The input node is not in the limits')
        input_initial_state()
    return input_node


# To get goal state from the user
def input_goal_state():
    goal_node = input('Enter the goal state with space : ')
    goal_node = tuple(int(j) for j in goal_node.split(" "))
    print(goal_node)
    if goal_node in obstacle_space:
        print('The given node is in obstacle space')
        input_goal_state()
    if goal_node[0] > 600 or goal_node[1] > 250 or goal_node[0] < 0 or goal_node[1] < 0:
        print('The goal node is not in the limits')
        input_goal_state()
    return goal_node

# To move up
def ActionMoveUp(pos, queue, goal):
    global index
    if queue != goal: 
        current_position = (pos[0], pos[1]+1)
        cost2_come = queue[0] +1
        index += 1
        parent_node = queue[1]
        node = (cost2_come, index, parent_node, current_position)
        if current_position not in visited_nodes and current_position not in obstacle_space:
            for i in range(queue_nodes.qsize()):
                if queue_nodes.queue[i][3] == current_position:
                    if queue_nodes.queue[i][0] > cost2_come:
                        index += 1
                        queue_nodes.queue[i] = (cost2_come, index, parent_node, current_position)
                        path_dict[queue_nodes.queue[i][3]] = pos
                        return
                    else:
                        return
            queue_nodes.put(node)
            path_dict[current_position] = pos
    return 

# To move down
def ActionMoveDown(pos, queue, goal):
    global index
    if queue != goal:
        current_position = (pos[0], pos[1]-1)
        cost2_come = queue[0] +1
        index += 1
        parent_node = queue[1]
        node = (cost2_come, index, parent_node, current_position)
        if current_position not in visited_nodes and current_position not in obstacle_space:
            for i in range(queue_nodes.qsize()):
                if queue_nodes.queue[i][3] == current_position:
                    if queue_nodes.queue[i][0] > cost2_come:
                        index += 1
                        queue_nodes.queue[i] = (cost2_come, index, parent_node, current_position)
                        path_dict[queue_nodes.queue[i][3]] = pos
                        return
                    else:
                        return
            queue_nodes.put(node)
            path_dict[current_position] = pos
    return 

# To move right
def ActionMoveRight(pos, queue, goal):
    global index
    if queue != goal:
        current_position = (pos[0]+1, pos[1])
        cost2_come = queue[0] +1
        index += 1
        parent_node = queue[1]
        node = (cost2_come, index, parent_node, current_position)
        if current_position not in visited_nodes and current_position not in obstacle_space:
            for i in range(queue_nodes.qsize()):
                if queue_nodes.queue[i][3] == current_position:
                    if queue_nodes.queue[i][0] > cost2_come:
                        index += 1
                        queue_nodes.queue[i] = (cost2_come, index, parent_node, current_position)
                        path_dict[queue_nodes.queue[i][3]] = pos
                        return
                    else:
                        return
            queue_nodes.put(node)
            path_dict[current_position] = pos
    return 

# To move left
def ActionMoveLeft(pos, queue, goal):
    global index
    if queue != goal:
        current_position = (pos[0]-1, pos[1])
        cost2_come = queue[0] +1
        index += 1
        parent_node = queue[1]
        node = (cost2_come, index, parent_node, current_position)
        if current_position not in visited_nodes and current_position not in obstacle_space:
            for i in range(queue_nodes.qsize()):
                if queue_nodes.queue[i][3] == current_position:
                    if queue_nodes.queue[i][0] > cost2_come:
                        index += 1
                        queue_nodes.queue[i] = (cost2_come, index, parent_node, current_position)
                        path_dict[current_position] = pos
                        return
                    else:
                        return
            queue_nodes.put(node)
            path_dict[current_position] = pos
    return 

# To move up and right diagonally
def ActionMoveUpRight(pos, queue, goal):
    global index
    if queue != goal:
        current_position = (pos[0]+1, pos[1]+1)
        cost2_come = queue[0] + 1.4
        index += 1
        parent_node = queue[1]
        node = (cost2_come, index, parent_node, current_position)
        if current_position not in visited_nodes and current_position not in obstacle_space:
            for i in range(queue_nodes.qsize()):
                if queue_nodes.queue[i][3] == current_position:
                    if queue_nodes.queue[i][0] > cost2_come:
                        index += 1
                        queue_nodes.queue[i] = (cost2_come, index, parent_node, current_position)
                        path_dict[queue_nodes.queue[i][3]] = pos
                        return
                    else:
                        return
            queue_nodes.put(node)
            path_dict[current_position] = pos
    return 

# To move up and left diagonally
def ActionMoveUpLeft(pos, queue, goal):
    global index
    if queue != goal:
        current_position = (pos[0]-1, pos[1]+1)
        cost2_come = queue[0] + 1.4
        index += 1
        parent_node = queue[1]
        node = (cost2_come, index, parent_node, current_position)
        if current_position not in visited_nodes and current_position not in obstacle_space:
            for i in range(queue_nodes.qsize()):
                if queue_nodes.queue[i][3] == current_position:
                    if queue_nodes.queue[i][0] > cost2_come:
                        index += 1
                        queue_nodes.queue[i] = (cost2_come, index, parent_node, current_position)
                        path_dict[queue_nodes.queue[i][3]] = pos
                        return
                    else:
                        return
            queue_nodes.put(node)
            path_dict[current_position] = pos
    return 

# To move down and right diagonally
def ActionMoveDownRight(pos, queue, goal):
    global index
    if queue != goal:
        current_position = (pos[0]+1, pos[1]-1)
        cost2_come = queue[0] + 1.4
        index += 1
        parent_node = queue[1]
        node = (cost2_come, index, parent_node, current_position)
        if current_position not in visited_nodes and current_position not in obstacle_space:
            for i in range(queue_nodes.qsize()):
                if queue_nodes.queue[i][3] == current_position:
                    if queue_nodes.queue[i][0] > cost2_come:
                        index += 1
                        queue_nodes.queue[i] = (cost2_come, index, parent_node, current_position)
                        path_dict[queue_nodes.queue[i][3]] = pos
                        return
                    else:
                        return
            queue_nodes.put(node)
            path_dict[current_position] = pos
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
        if current_position not in visited_nodes and current_position not in obstacle_space:
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

# For back tracking to initial position
def back_tracking(path, initial_state, pre_queue):
    queue_pop_tup = pre_queue[3]
    queue_pop_initial = initial_state[3]
    best_path.append(queue_pop_tup)
    parent_node = path[queue_pop_tup]
    best_path.append(parent_node)
    # Finding the parent of parent to back track

    while parent_node != queue_pop_initial:  
        parent_node = path[parent_node]
        best_path.append(parent_node)
        if pre_queue == queue_pop_initial:
            parent_node = path[queue_pop_tup]
            best_path.append(parent_node)
            break
    best_path.reverse()
    print("Path Taken: ")
    for i in best_path:
        print(i)
    return best_path


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
        d = back_tracking(path_dict, node_state_i, queue_pop)
        print("Goal Reached: ", node_state_g)
        break

end_time = time.time()
elapsed_time = end_time - start_time
print('Execution time:', elapsed_time, 'seconds')
game(visited_nodes, best_path)

