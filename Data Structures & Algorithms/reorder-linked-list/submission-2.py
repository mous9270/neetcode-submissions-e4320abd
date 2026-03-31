# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow=head, head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        t=slow.next
        slow.next=None
        l1, c=head, t
        prev=None
        while c:
            t=c.next
            c.next=prev
            prev=c
            c=t
        l2=prev
        
        while l2:
            t1=l1.next
            l1.next=l2
            l2=l2.next
            l1=l1.next
            l1.next=t1
            l1=l1.next
        
        

