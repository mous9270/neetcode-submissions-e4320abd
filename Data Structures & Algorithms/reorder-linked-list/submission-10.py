# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        c=slow.next
        slow.next=None
        prev=None
        while c:
            t=c.next
            c.next=prev
            prev=c
            c=t
        l1,l2=head, prev
        while l1 and l2:
            t1, t2=l1.next, l2.next
            l1.next=l2
            l2.next=t1
            l1,l2=t1,t2

