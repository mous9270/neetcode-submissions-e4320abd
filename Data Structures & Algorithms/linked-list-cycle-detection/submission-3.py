# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        m={}
        curr=head
        while curr:
            if curr in m:
                return True
            else:
                m[curr]=0
                curr=curr.next
        return False
        