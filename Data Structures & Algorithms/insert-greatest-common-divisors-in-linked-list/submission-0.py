# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            gcd_val = math.gcd(cur.val, cur.next.val)
            gcd_node = ListNode(gcd_val)
            gcd_node.next = cur.next
            cur.next = gcd_node
            cur = gcd_node.next
        return head
            
