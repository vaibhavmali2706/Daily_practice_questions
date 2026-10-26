class ListNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        if not head or left==right:
            return head
        
        dummy=ListNode(0)
        prev=dummy
        dummy.next=head
        for _ in range(left-1): 
            prev=prev.next
        temp=prev.next
        for _ in range (right-left):
            do = temp.next
            temp.next = do.next
            do.next = prev.next
            prev.next = do
        return dummy.next.val
a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
a.next=b
b.next=c
c.next=d
s=Solution()
print(s.reverseBetween(a,1,3))