# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # if len(lists)==0:
        #     return []
        # if len(lists)==1:
        #     return lists[0]
        for i in range(1, len(lists)):
            lists[0]=self.merge(lists[0], lists[i])
        return lists[0] if lists else None
    def merge(self,l1, l2):
        curr=ans=ListNode()
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