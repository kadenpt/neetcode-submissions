# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current, res = head, head
        length = 1
        while current.next:
            length += 1
            current = current.next
        
        removeIndex = length - n
        if removeIndex == 0:
            return head.next

        current = head
        for i in range(length - 1):
            if (i + 1) == removeIndex:
                current.next = current.next.next
                break
            current = current.next

        return head