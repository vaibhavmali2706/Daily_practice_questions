class ListNode:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next
class Solution:
    def removefromend(self, head, n):
        cnt = 0
        temp = head

        while temp:
            cnt += 1
            temp = temp.next

        tar = cnt - n + 1
        if tar == 1:
            return head.next
        temp = head

        for i in range(1, tar - 1):
            temp = temp.next
        temp.next = temp.next.next

        return head

A=ListNode(10)
B=ListNode(20)
C=ListNode(30)
D=ListNode(40)
head=A
A.next=B
B.next=C
C.next=D
print(Solution().removefromend(head,2))