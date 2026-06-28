# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. 快慢指针找中点,slow 停在前半段的尾
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 反转后半段
        second = slow.next
        slow.next = None        # 从中间断开,前半段收尾
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        second = prev           # prev 是反转后那半的头(原链表尾)

        # 3. 交替合并两条
        first = head
        while second:
            f_nxt = first.next      # 先存好两边的下一个
            s_nxt = second.next
            first.next = second     # first → second
            second.next = f_nxt     # second → 原 first 的下一个
            first = f_nxt
            second = s_nxt