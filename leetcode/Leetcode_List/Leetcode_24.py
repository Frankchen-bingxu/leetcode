# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode(0)
        dummy.next = head
        
        pre = dummy
        
        while pre.next is not None and pre.next.next is not None:
            #store the val
            node1 = pre.next
            
            node2 = pre.next.next
            
            #swap,link,node2.next must given at last of the exchange process
            pre.next = node2
            node1.next = node2.next
            
            node2.next = node1
            
            pre = pre.next.next
            
        return dummy.next
            
        
        