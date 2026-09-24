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

class Solution:
    def isPalindrome(self, head):
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
sol = Solution()
print(sol.isPalindrome(root))