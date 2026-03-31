# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow=head.next, head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        m=slow.next
        slow.next=None
        l1, l2= head, m
        prev=None
        curr=l2
        while curr:
            t=curr.next
            curr.next=prev
            prev=curr
            curr=t
        l3=prev
        while l3:
            t=l1.next
            l1.next=l3
            l3=l3.next
            l1=l1.next
            l1.next=t
            l1=l1.next

        