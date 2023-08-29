colors = [['red', 'green', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]


measurements = ['green', 'green', 'green', 'green', 'green']

# image matching --------------------------------------------------------------?????????????????????????????!!!!!!!!

motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]

sensor_right=0.7
p_move=0.8


n1=len(colors)
n2=len(colors[0])
dist=1/(n1*n2)
p=[]
for x in range(len(colors)):
    p.append([])
    for y in range(len(colors[1])):
        p[x].append(dist)


def sense(p,Z):
    q=[]
    for i in range(len(p)):
        q.append([])
        for j in range(len(p[0])):
            h = Z == colors[i][j]
            q[i].append(p[i][j]*h*sensor_right+p[i][j]*(1-h)*(1-sensor_right))
    sumo = sum(sum(q, []))
    for i in range(len(p)):
        for j in range(len(p[0])):
            q[i][j]=q[i][j]/sumo
    return q


def move(p,U):
    q=[]
    for i in range(len(p)):
        q.append([])
        for j in range(len(p[0])):

            q[i].append(p[(i-U[0]) % len(p)][(j-U[1]) % len(p[i])]*p_move+p[i][j]*(1-p_move))

    return q


for j in range(len(motions)):
    p = move(p, motions[j])
    p = sense(p, measurements[j])


for h in range(len(p)):
    print(p[h])

