grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init=[4, 3, 0] #first two elements are coordinates, third is direction

goal = [2, 0]

forward=[[-1, 0],   # go up
       [0, -1],   # go left
       [1, 0],    # go down
       [0, 1]]    # go right

forward_name = ['up', 'left', 'down', 'right']

#the cost field has 3 values: right turn, no turn, left turn
cost=[2, 1, 1]
action=[-1, 0, 1]
action_name = ['R', '#', 'L']

# -------------------------------------------------------------------

value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
        [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
        [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
        [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]

policy = [[[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
        [[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
        [[' ' for row in range(len(grid[0]))] for col in range(len(grid))],
        [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]]

policy2D = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

change = True
while change:
    change = False

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for orientation in range(4):

                if goal[0] == x and goal[1] == y:

                    if value[orientation][x][y] > 0:
                        change = True
                        value[orientation][x][y] = 0
                        policy[orientation][x][y] = '*'

                elif grid[x][y] == 0:
                    for i in range(len(action)):
                        o2 = (orientation + action[i]) % 4
                        x2 = x + forward[o2][0]
                        y2 = y + forward[o2][1]

                        # print(z2)

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            # print(value[z2][x2][y2])
                            v2 = value[o2][x2][y2] + cost[i]

                            if v2 < value[orientation][x][y]:
                                value[orientation][x][y] = v2
                                # print(value[x][y][z])
                                policy[orientation][x][y] = action_name[i]
                                change = True
#for i in range(len(policy)):
#   print(policy[i])

x = init[0]
y = init[1]
orientation = init[2]

policy2D[x][y] = policy[orientation][x][y]
while policy[orientation][x][y] != '*':
    if policy[orientation][x][y] == '#':
        o2 = orientation
    elif policy[orientation][x][y] == 'R':
        o2 = (orientation - 1) % 4
    elif policy[orientation][x][y] == 'L':
        o2 = (orientation + 1) % 4
    x = x + forward[o2][0]
    y = y + forward[o2][1]
    orientation = o2
    policy2D[x][y] = policy[orientation][x][y]

for i in range(len(policy2D)):
    print(policy2D[i])

