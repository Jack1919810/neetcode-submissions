# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()   # 哑头,纯占位,最后 return dummy.next
        tail = dummy         # 结果表的尾,一直往后接
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # 尾巴往前挪
        tail.next = list1 if list1 else list2  # 谁还剩,整条接上
        return dummy.next