from structure import TreeNode, dump_tree, gen_tree

# traceback /DFS templater
# result = []
# def backtrack(路径, 选择列表):
#     if 满足结束条件:
#         result.add(路径)
#         return

#     for 选择 in 选择列表:
#         做选择
#         backtrack(路径, 选择列表)
#         撤销选择

# BFS template
# def BFS(start, target):
#     queue = [start]
#     visited = set()
#     visited.add(start)
#     step = 0

#     while len(queue) > 0:
#         sz = len(queue)
#         cur = queue.pop(0)
#         for i in range(sz):
#             for j in i.around-node
#                 if n not in visited:
#                     queue.append(n)
#                     visited.add(n)
#         step += 1

disp = []
def permute(arr):
    if len(disp) == len(arr):
        print(disp)
        return
    for itm in arr:
        if itm in disp:
            continue
        disp.append(itm)
        permute(arr)
        disp.pop()

def queen_judge(vec):
    row = len(vec)
    col = len(vec[0])
    for i in range(row):
        sum = 0
        for j in range(col):
            sum += vec[i][j]
        if sum != 1:
            return 0
    for i in range(col):
        sum = 0
        for j in range(row):
            sum += vec[j][i]
        if sum != 1:
            return 0
    for i in range(row):
        for j in range(col):
            if 1 == vec[i][j]:
                sum = 0
                if i-1 >= 0:
                    if j-1 >= 0:
                        sum += vec[i-1][j-1]
                    if j+1 < col:
                        sum += vec[i-1][j+1]
                if i+1 < row:
                    if j-1 >= 0:
                        sum += vec[i+1][j-1]
                    if j+1 < col:
                        sum += vec[i+1][j+1]
                if 0 != sum:
                    return 0
    return 1

def nqueen(vec, row):
    if row == len(vec):
        if queen_judge(vec) == 1:
            print(vec)
            return 1
        else:
            return 0
    for col in range(len(vec[row])):
        vec[row][col] = 1
        nqueen(vec, row+1)
        vec[row][col] = 0

# more efficient way than nqueen
def nqueen2_is_valid(vec, row, col):
    n = len(vec)
    for i in range(n):
        if vec[row][i] == 1:
            return -1
        if vec[i][col] == 1:
            return -1            
    # if row-1 >= 0:
    #     if col-1 >= 0 and vec[row-1][col-1] == 1:
    #         return -1
    #     if col+1 < n and vec[row-1][col+1] == 1:
    #         return -1
    # if row+1 < n:
    #     if col-1 >= 0 and vec[row+1][col-1] == 1:
    #         return -1
    #     if col+1 < n and vec[row+1][col+1] == 1:
    #         return -1
    for i in range(row):
        delta = row - i
        if col - delta >= 0 and vec[i][col-delta] == 1:
            return -1
        if col + delta < n and vec[i][col+delta] == 1:
            return -1
    
    return 0

total = 0    
def nqueen2(vec, row):
    global total
    if row == len(vec):
        total += 1
        for i in range(row):
            print(vec[i])
        print('-------', total)
        return

    col = len(vec[row])
    for i in range(col):
        if nqueen2_is_valid(vec, row, i) < 0:
            continue
        vec[row][i] = 1
        nqueen2(vec, row+1)
        vec[row][i] = 0

def min_depth_bfs(tree):
    q = [tree]
    v = set()

    depth = 1
    while len(q):
        sz = len(q)
        for i in range(sz):
            node = q.pop(0)
            if None == node.left and None == node.right:
                print('depth = %d' %depth)
                return
            if node.left:    
                q.append(node.left)
            if node.right:
                q.append(node.right)

        depth += 1
    print(depth)

def switch_one(dig,up,idx):
    val = int(dig)
    inc = 10**idx
    if up > 0:
        if (val // inc)%10 == 9:
            val -= 9*inc
        else:
            val += inc
    else:
        if (val // inc)%10 == 0:
            val += 9*inc
        else:
            val -= inc
    return "%04d" %val


def openlock(dead, target):
    q = ['0000']
    v = {'0000':'end'}
    depth = 1
    while len(q):
        sz = len(q)
        for i in range(sz):
            cur = q.pop(0)
            for j in range(4): 
                for k in range(2):
                    switch = switch_one(cur, k, j)

                    if switch in v:
                        continue
                    if switch not in dead:
                        q.append(switch)
                        v[switch] = cur
                    if target == switch:
                        print('depth = %d' %depth)
                        while switch in v:
                            print('%s <-' %switch, sep='')
                            switch = v[switch]
                        return
                        
        depth += 1


    
if __name__ == '__main__':
    #permute([1,2,3,4])
    #nqueen2([[0 for i in range(8)] for j in range(8)],0)

    # root = gen_tree([1,2,3,4,5,6,7,8,9,10,11,None, None, 12,13])
    # dump_tree(root)
    # min_depth_bfs(root)
    # dump_tree(root)

    openlock(['0201','0101','0102','1212','2002'], '0202')
    # openlock(['8887','8889', '8878','8898','8788','8988','7888','9888',], '8888')
    #switch_one('0192', 1, 1)