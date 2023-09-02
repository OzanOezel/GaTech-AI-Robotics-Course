from math import *

path = [[0, 0], # fix
        [1, 0],
        [2, 0],
        [3, 0],
        [4, 0],
        [5, 0],
        [6, 0], # fix
        [6, 1],
        [6, 2],
        [6, 3], # fix
        [5, 3],
        [4, 3],
        [3, 3],
        [2, 3],
        [1, 3],
        [0, 3], # fix
        [0, 2],
        [0, 1]]

fix = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]

def smooth(path, fix, weight_data = 0.0, weight_smooth = 0.1, tolerance = 0.000001):

    newpath = [[0 for col in range(len(path[0]))] for row in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]
    tolerance = 0.000001
    change = tolerance
    while change >= tolerance:
        change = 0.0
        for i in range(len(path)):
            if not fix[i]:
                for j in range(len(path[0])):
                    aux = newpath[i][j]
                    newpath[i][j] += weight_data * (path[i][j] - newpath[i][j])
                    newpath[i][j] += weight_smooth * (
                                newpath[(i + 1) % len(newpath)][j] + newpath[(i - 1) % len(newpath)][j] -
                                2 * newpath[i][j])
                    newpath[i][j] += weight_smooth/2 * (2*newpath[(i - 1) % len(newpath)][j] -
                                                        newpath[(i - 2) % len(newpath)][j] -
                                                        newpath[(i) % len(newpath)][j])
                    newpath[i][j] += weight_smooth / 2 * (2 * newpath[(i + 1) % len(newpath)][j] -
                                                          newpath[(i + 2) % len(newpath)][j] -
                                                          newpath[(i) % len(newpath)][j])
                    change += abs(aux - newpath[i][j])
    return newpath


newpath = smooth(path, fix)

for i in range(len(path)):
    print('[' + ', '.join('%.3f' % x for x in path[i]) + '] -> [' + ', '.join('%.3f' % x for x in newpath[i]) + ']')
