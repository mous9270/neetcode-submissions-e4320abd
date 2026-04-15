# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head, head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        l=slow.next
        slow.next=None
        prev=None
        while l:
            t=l.next
            l.next=prev
            prev=l
            l=t
        l1=head
        l2=prev
        while l1 and l2:
            t=l1.next
            l1.next=l2
            l2=l2.next
            l1=l1.next
            l1.next=t
            l1=l1.next
        
        

            
