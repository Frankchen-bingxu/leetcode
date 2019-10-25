# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        #brute force
#         self.nodes = []
#         head = point = ListNode(0)
        
#         for l in lists:
#             while l:
#                 self.nodes.append(l.val)
#                 l = l.next
#         for x in sorted(self.nodes):
#             point.next = ListNode(x)
#             point = point.next
#         return head.next
        
        #Using divide and conquer method
        
    def mergeKLists(self, lists):
        # recursive
        if lists is None:
            return None
        elif len(lists) == 0:
            return None
        return self.mergeK(lists, 0, len(lists) - 1)

    
    def mergeK(self, lists, low, high):
        if low == high:
            return lists[low]
        elif low + 1 == high:
            return self.mergeTwolists(lists[low], lists[high])
        mid = (low + high) / 2
        return self.mergeTwolists(self.mergeK(lists, low, mid), self.mergeK(lists, mid + 1, high))

    
    def mergeTwolists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        head = curr = ListNode(0)
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1 is not None:
            curr.next = l1
        if l2 is not None:
            curr.next = l2
        return head.next