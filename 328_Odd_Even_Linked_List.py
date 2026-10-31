class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class SinglyLikedList:
    def __init__(self):
        self.head=None
    def Insert_at_end(self,value):
        new_node=ListNode(value)
        if self.head is None:
            self.head = new_node
            return self.head
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        return self.head 
    def display(self):
        temp = self.head

        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next

        print("None")
            

class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        odd = head
        even = head.next
        while even and even.next:
            odd.next=odd.next.next
            odd=odd.next
            even=even.next.next
            even=even.next
        return head


si=SinglyLikedList()


si.Insert_at_end(10)
si.Insert_at_end(20)
si.Insert_at_end(30)
si.Insert_at_end(40)
si.Insert_at_end(50)

si.display()

print("after")

s=Solution()
s.oddEvenList(si.head)
            