# path = [city1, city3, city4, city2, city1]
# citylist = [city1, city2, city3, city4]


citylist = []
# finds fitness of path
def fitness(mat, path):
    sum = 0
    path.append(path[0])
    for i in range(len(path)-1):
        start = citylist.index(path[i])
        end = citylist.index(path[i+1])
        if mat[start][end] == 0:
            return 0
        else:
            sum += mat[start][end]
    return sum

# creates list of paths 1 swap away from current path
def alter(path):
    alteredlist = []

    for i in range(len(path)-1):
        for j in range(i+1, len(path)):
            alteredpath = path
            temp = alteredpath[i]
            alteredpath[i] = alteredpath[j]
            alteredpath[j] = temp
    return alteredlist

def tabu_search(mat, max_iters, tabu_list_size, initial):
    bestpath = initial
    bestfit = fitness(mat, bestpath)
    tabu_list = []
    for i in range(max_iters):
        altered = alter(bestpath)
        for newpath in altered:
            newfit = fitness(mat, newpath)
            #check if path is in tabulist
            if newpath in tabu_list:
                continue
            else:
                # bad path is found
                if newfit == 0:
                    if len(tabu_list) >= tabu_list_size:
                        tabu_list.remove(0)
                    tabu_list.append(newpath)
                    continue
                # need to tune accept condition
                elif newfit <= bestfit * 1.01:
                    bestpath = newpath
                    bestfit = newfit
                # worse path is found
                else:
                    if len(tabu_list) >= tabu_list_size:
                        tabu_list.remove(0)
                    tabu_list.append(newpath)
                    continue
    return bestpath.append(bestpath[0])