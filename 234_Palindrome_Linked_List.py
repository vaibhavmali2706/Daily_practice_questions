class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


root=ListNode(1)
node2=ListNode(1)
node3=ListNode(2)
node4=ListNode(3)
node5=ListNode(3)
root.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

curr=root
while curr and curr.next:
    curr=curr.next
