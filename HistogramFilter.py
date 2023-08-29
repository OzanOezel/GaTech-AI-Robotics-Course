p=[0.2,0.2,0.2,0.2,0.2]
world=['green','red','red','green','green']
Measurements = ['red', 'red']
motions=[1,1]
pHit=0.6
pMiss=0.2
pExact=0.8
pOvershoot=0.1
pUndershoot=0.1

def sense(p,Z):
    q=[]
    for i in range(len(p)):
        j= Z==world[i]
        q.append(-p[i]*pMiss*(j-1)+p[i]*pHit*(j))
    sumo= sum(q)
    for i in range(len(q)):
        q[i]=q[i]/sumo
    return q

def move(p, U):
    q=[]
    for i in range(len(p)):
        q.append(p[(i-U) % len(p)]*pExact + p[(i-U-1) % len(p)]*pOvershoot + p[(i-U+1) % len(p)]*pUndershoot)

    return q

for j in range(len(Measurements)):
    p = sense(p, Measurements[j])
    p=move(p,motions[j])


print(p)
