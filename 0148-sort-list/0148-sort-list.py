# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None    
        
        left=self.sortList(head)
        right=self.sortList(slow)
        
        res=self.merge(left,right)
        
        return res
    
    def merge(self,left,right):
        dummy=ListNode()
        cur=dummy
        
        while(left and right):
            if left.val<=right.val:
                cur.next=ListNode(left.val)
                left=left.next
            else:
                cur.next=ListNode(right.val)
                right=right.next
            cur=cur.next
                
        if left:
            cur.next=left
        if right:
            cur.next=right
            
        return dummy.next
        
                
        
        
            