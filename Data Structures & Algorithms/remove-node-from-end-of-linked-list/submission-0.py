# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = 0
        curr = head
        while curr:
            dummy += 1
            curr = curr.next
        delNode = dummy - n
        if delNode == 0:
            return head.next
        
        curr = head
        for i in range(dummy - 1):
            if (i+1) == delNode:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head