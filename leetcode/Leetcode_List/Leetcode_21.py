# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        
        #Method1:compare two list from the first node of the list
#         if not l1 or not l2:
#             return l1 or l2
        
#         result = current = ListNode(0)
        
#         while l1 and l2:
#             if l1.val < l2.val:
#                 current.next = l1
#                 l1 = l1.next
#             else:
#                 current.next = l2
#                 l2 = l2.next
            
#             current = current.next
        
#         current.next = l1 or l2
        
#         return result.next
          
    
        #Method2: Using recursion idea
        
        if l1 is None:
            return l2
        elif l2 is None:
            return l1 
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
    