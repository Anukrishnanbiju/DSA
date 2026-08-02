# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev = dummy

        while True:

            
            kth = prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next

        
            cur = prev.next
            pre = groupNext

            while cur != groupNext:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            temp = prev.next
            prev.next = kth
            prev = temp