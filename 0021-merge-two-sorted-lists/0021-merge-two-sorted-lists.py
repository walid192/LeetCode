# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode()
        current=dummy
        
        while(l1 or l2):
            if (l1 and l2 and l1.val<=l2.val):
                current.next=ListNode(l1.val)
                l1=l1.next
            elif(l1 and l2 and l1.val>l2.val):
                current.next=ListNode(l2.val)
                l2=l2.next
            elif (l1):
                current.next=l1
                l1=None
            else:
                current.next=l2
                l2=None
                
            current=current.next
            
        return dummy.next
                
                
                
            
        