# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next        # 慢的走一步
            fast = fast.next.next   # 快的走两步
            if slow is fast:        # 套圈了 = 有环
                return True
        return False