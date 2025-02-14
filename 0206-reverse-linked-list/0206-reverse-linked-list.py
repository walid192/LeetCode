# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev=head

        current=head.next
        prev.next=None

        while current:
            nextNode=current.next
            current.next=prev
            prev=current
            current=nextNode

        return prev
        