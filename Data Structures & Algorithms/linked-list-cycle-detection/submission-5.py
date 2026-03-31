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
            if curr.next not in m:
                m[curr.next]=0
                curr=curr.next
            else:
                return True
        return False