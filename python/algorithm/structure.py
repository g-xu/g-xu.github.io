# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = None


def dump_list(head):
    p = head
    while(p):
        print(p.val)
        p = p.next
    print('------')

def gen_list(count) -> ListNode:
    p = head = ListNode(val=0)
    for i in range(1, count):
        p.next = ListNode(i)
        p = p.next
    return head

def dump_tree(root):
    if None == root:
        return
    cur_line = 0
    tl = [[root, cur_line]]
    while len(tl):
        node, line = tl.pop(0)
        if line != cur_line:
            cur_line = line
            print()
        if isinstance(node, TreeNode):
            print(node.val, end='    ')
            if node.left:
                tl.append([node.left, line+1])
            else:
                tl.append(['#', line+1])
            if node.right:
                tl.append([node.right, line+1])
            else:
                tl.append(['#', line+1])
        else:
            print(node, end='    ')
    print()
            

    

#generate tree from list as [1,2,3,4,None,6,7]
def gen_tree(tl):
    if len(tl) == 0:
        return None

    root = TreeNode(tl[0])
    nlist = [root,]
    for i in range(1,len(tl)):
        if tl[i]:
            node = TreeNode(tl[i])
            nlist.append(node)
            if 1 == i % 2:
                nlist[(i-1)//2].left = node
            else:
                nlist[(i-1)//2].right = node

    return root




if __name__ == '__main__':
    root = gen_tree([1,2,3])
    dump_tree(root)