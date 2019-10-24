# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #consruct a dummy that if remove the first node. the list is not empty
        dummy = ListNode(0)
        dummy.next = head
        
        #get length of the List,current is the node before the remove node
        pre = dummy
        length = 0
        
        while pre.next:
            length += 1 
            pre = pre.next
            
        
        pre = dummy
        count  = 1
        while pre.next: #if the list is not the empty list
            current = pre.next #count form the first node=1.final the current is the node to removed，length - n +1 is counted from the first of the list,ex.length = 5 , n=2 ,the count form the first is 4 = 5-2+1
            if count == length - n + 1:
                pre.next = current.next #current 
                break
            else:
                pre = pre.next #pre is the node pre at current 
                count += 1 

        return dummy.next
  