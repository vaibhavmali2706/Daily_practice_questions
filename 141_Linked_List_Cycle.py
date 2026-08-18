class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return slow.val
        
        return False
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
root = ListNode(3)
r1 = ListNode(2)
r2 = ListNode(0)
r3 = ListNode(-4)
r4 = ListNode(5)
root.next = r1
r1.next = r2
r2.next = r3
r3.next = r1  # Creating a cycle here
r4.next = None  # This node is not part of the cycle

s = Solution()
print(s.hasCycle(root))  # Output: True 