class Solution(object):

    def reverseNode(self, head):
        prev,current=None,head
        while (current):
            next_node=current.next
            current.next=prev
            prev,current=current,next_node

        return prev


    def doubleIt(self, head):
        newHead=self.reverseNode(head)
        
        carry=0
        prev,current=None,newHead

        while(current):
            value=current.val*2+carry
            next_node=current.next

            current.val=value%10
            carry=value//10

            prev,current=current,next_node

        if(carry):
            prev.next=ListNode(1)

        res=self.reverseNode(newHead)

        return res
    


        
    
    
