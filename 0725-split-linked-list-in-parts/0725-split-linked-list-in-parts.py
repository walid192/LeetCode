# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = 0
        dummy = head
        while dummy:
            l += 1
            dummy = dummy.next

        segment_length = l // k
        remainder = l % k

        res = [None] * k

        current = head
        for i in range(k):
            if not current:
                res[i] = None
                continue

            res[i] = current
            part_size = segment_length + (1 if remainder > 0 else 0)
            remainder -= 1

            for j in range(part_size - 1):
                if current:
                    current = current.next

            if current:
                temp = current.next
                current.next = None
                current = temp

        return res
