# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast,slow= head, head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        m=slow.next
        slow.next=None
        prev=None
        
        while m:
            t=m.next
            m.next=prev
            prev=m
            m=t
        l1, l2=head, prev
        while l2:
            t=l1.next
            l1.next=l2
            l2=l2.next
            l1=l1.next
            l1.next=t
            l1=l1.next
            