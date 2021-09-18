
from structure import TreeNode, dump_tree, gen_tree

#遍历二叉树模板
def traverse_tree(root):
    traverse_tree(root.left)
    traverse_tree(root.right)


#二叉树镜像翻转
def btree_mirror(root):
    if not root:
        return None
    right = root.right
    root.right = root.left
    root.left = right
    btree_mirror(root.right)
    btree_mirror(root.left)

#二叉树右侧指针
def connect_node(node1, node2):
    if not node1 or not node2:
        return
    node1.next = node2
    connect_node(node1.left, node1.right)
    connect_node(node1.right, node2.left)
    connect_node(node2.left, node2.right)
def btree_next(root):
    if not root:
        return None
    connect_node(root.left, root.right)
    return root

def btree_flatten(root):
    if None == root:
        return None
    
    btree_flatten(root.left)
    btree_flatten(root.right)

    left = root.left
    right = root.right
    root.left = None
    root.right = left

    p = root
    while p.right != None:
        p = p.right
    p.right = right

    return 


def coinchange(coins, amount):
    # template
    # def dp(n):
    #     for coin in coins:
    #         res = min(res, 1+dp(n-coin))
    #     return res
    # return dp(amount)

    memo = {}
    def dp(n):
        if n == 0: 
            return 0
        if n < 0: 
            return -1
        if n in memo:
            return memo[n]

        res = 1000
        for coin in coins:
            sub = dp(n - coin)
            if sub < 0:
                continue
            res = min(res, sub+1)
        
        if res < 0:
            return -1
        else:
            memo[n] = res
            print(memo)
            return res
        
    return dp(amount)

def coinchange_dp(coins, amount):
    dp = [amount+1] * (amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if i - coin < 0: continue
            dp[i] = min(dp[i], dp[i-coin]+1)
    print(dp)
    return dp[amount] if (dp[amount] != amount + 1) else -1

def test():
    # root = gen_tree([1,2,3,4,5,6])
    # dump_tree(root)
    # btree_mirror(root)
    # dump_tree(root)

    # root = gen_tree([1,2,3,4,5,6,7])
    # btree_next(root)
    # dump_tree(root)

    # root = gen_tree([1,2,3,4,5,6,7])
    # btree_flatten(root)
    # dump_tree(root)
    
    # step = coinchange([1,2,5], 50)
    # print('step: %d' %step)

    step = coinchange_dp([3,2,7], 50)
    print('step: %d' %step)


if __name__ == '__main__':
    test()