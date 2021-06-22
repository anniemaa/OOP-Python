# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while(curr is not None):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
    """

    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverse(head, None)

    def reverse(self, head, newHead):
        if head is None:
            return newHead
        tmp = head.next
        head.next = newHead
        newHead = head
        head = tmp

        return self.reverse(head, newHead)
