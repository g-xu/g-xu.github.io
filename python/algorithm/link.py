

from structure import ListNode,dump_list,gen_list


###
## 递归倒序链表模板
###
def reverse_list(head):
    if head.next == None:
        return head
    last = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return last

###
## 指针倒序列表
###
def reverse_list_pointer(head):
    (prev, cur) = (None, head)
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    return prev


successor = None
def reverse_nth(head, n):
    global successor
    if 1 == n:
        successor = head.next
        return head
    last = reverse_nth(head.next, n-1)
    head.next.next = head
    head.next = successor
    return last

def test():
    head = gen_list(10)
    dump_list(head)
    # head = reverse_list(head)
    # head = reverse_nth(head, 4)
    head = reverse_list_pointer(head)
    dump_list(head)

if __name__ == '__main__':
    test()