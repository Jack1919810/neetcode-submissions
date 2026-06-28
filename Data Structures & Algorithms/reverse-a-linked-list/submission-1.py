# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None          # 新链表头,初始为空
        curr = head
        while curr:
            nxt = curr.next  # 先存好下一个,不然断了找不回去
            curr.next = prev # ← 头插:curr 接到新链表最前
            prev = curr      # 新链表头更新成 curr
            curr = nxt       # 继续摘旧链表下一个
        return prev          # prev 始终是新链表的头