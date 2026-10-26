class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev=None
        temp=head
        while(temp):
            do=temp.next
            temp.next=prev
            prev=temp
            temp=do
        return prev.data
a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
a.next=b
b.next=c
c.next=d
print(Solution().reverseList(a))
            
            
            
            
            
        