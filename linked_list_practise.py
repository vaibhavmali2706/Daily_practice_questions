class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = ListNode(1)
next_node = head.next
next_node = ListNode(2)
print(head.val)