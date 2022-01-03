INT_INF = 1e9

e = [[1,3,4],[0,2,4],[2,4,5],[0,4,6],[0,1,2,3,5,6,7,8],[2,4,8],[3,4,7],[4,6,8],[4,5,7]]


weight = [[0 if i == j else INT_INF for j in range(9)] for i in range(9)]
weight[0][1] = 1
weight[0][3] = 2
weight[0][4] = 5
weight[1][2] = 5
weight[1][4] = 3
weight[2][4] = 1
weight[2][5] = 2
weight[3][4] = 5
weight[3][6] = 4
weight[4][5] = 2
weight[4][6] = 2
weight[4][7] = 1
weight[4][8] = 2
weight[5][8] = 1
weight[6][7] = 3
weight[7][8] = 2

for i in range(9):
    for j in range(i,9):
        if weight[i][j] != INT_INF:
            weight[j][i] = weight[i][j]

dv = [[min(weight[i][j],weight[j][i]) for i in range(9)] for j in range(9)]

notified = [1 for i in range(9)]

print("0 Iteration:")
for i in range(9):
    print(chr(ord('A') + i)," table:")
    print(chr(ord('A') + i),end=" ")
    print("[%s]"%','.join([str(i) if i != INT_INF else "INF" for i in weight[i]]))
    for item in e[i]:
        print(chr(ord('A') + item),end=" ")
        print("[%s]"%','.join([str(i) if i != INT_INF else "INF" for i in weight[item]]))
    print("")

for run in range(1,9):
    flag = 0
    new_dv = [[dv[i][j] for j in range(9)] for i in range(9)]
    for i in range(9):
        new_notified = [0 for i in range(9)]

        if notified[i] == 0:
            continue

        notified[i] = 0
        fixed = 0
        for item in e[i]:
            for j in range(9):
                if weight[i][item] + dv[item][j] < dv[i][j]:
                    new_dv[i][j] = weight[i][item] + dv[item][j]
                    fixed = 1
        if fixed:
            flag = 1
            for item in e[i]:
                notified[item] = 1

    print(run," iterations:")

    for i in range(9):
        print(chr(ord('A') + i)," table:")
        print(chr(ord('A') + i),end=" ")
        print("[%s]"%','.join([str(i) if i != INT_INF else "INF" for i in new_dv[i]]))
        for item in e[i]:
            print(chr(ord('A') + item),end=" ")
            print("[%s]"%','.join([str(i) if i != INT_INF else "INF" for i in dv[item]]))
        print("")

    for i in range(9):
        for j in range(9):
            dv[i][j] = new_dv[i][j]

    if flag == 0:
        print("Unchanged. Break")
        break
    '''
    for i in range(9):
        print(chr(i+ord("A")),":<",end="")
        for j in range(9):
            if dv[i][j] == INT_INF:
                print("INF",end=",\0"[j==8])
            else:
                print(dv[i][j],end=",\0"[j==8])
            dv[i][j] = new_dv[i][j]
        print(">")

    '''


'''
print("Step 0:")
for i in range(9):
    print(chr(ord("A") + i)+":<",end="")
    for j in range(9):
        if(j <= i):
            weight[i][j] = weight[j][i]
        if(weight[i][j] == INT_INF):
            print(("INF,","INF")[j==8],end="")
        else:
            print(weight[i][j],end=(",","")[j==8])
    print(">")

for step in range(1,9):
    tmp_dv = [[dv[i][j] for i in range(9)] for j in range(9)]
    flag = True

    for u in range(9):
        for v in e[u]:
            for vertice in range(9):
                if dv[vertice][u] + weight[u][v] < dv[vertice][v]:
                    tmp_dv[vertice][v] = dv[vertice][u] + weight[u][v]
                    flag = False
                    #print(f"relax {vertice} to {v} from {dv[vertice][v]} to {tmp_dv[vertice][v]} by edge {u} {v}")

    dv = tmp_dv
    print(f"Step {step}:")

    for i in range(9):
        print(chr(ord("A") + i)+":<",end="")
        for j in range(9):
            if(j <= i):
                dv[i][j] = dv[j][i]
            if(dv[i][j] == INT_INF):
                print(("INF,","INF")[j==8],end="")
            else:
                print(dv[i][j],end=(",","")[j==8])
        print(">")

    if flag:
        print("No change, break.")
        break
'''
