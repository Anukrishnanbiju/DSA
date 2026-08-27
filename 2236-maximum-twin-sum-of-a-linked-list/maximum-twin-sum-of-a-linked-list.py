class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a = []

        while head:
            a.append(head.val)
            head = head.next

        n = len(a)
        return max(a[i] + a[n - 1 - i] for i in range(n // 2))