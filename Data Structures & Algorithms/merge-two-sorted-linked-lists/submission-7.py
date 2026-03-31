# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans=curr=ListNode()
        l1,l2=list1, list2
        while l1 and l2:
            if l1.val<l2.val:
                t=l1.next
                curr.next=l1
                curr=curr.next
                l1=t
            else:
                t=l2.next
                curr.next=l2
                curr=curr.next
                l2=t
        curr.next=l1 or l2
        return ans.next