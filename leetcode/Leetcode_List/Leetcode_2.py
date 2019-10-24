# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        #for debugging
        return repr(self.value)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Algorithm: Two pointers & math
        Two pointers for l1 and l2 respectively
        Math - carry for addition, in the form of new node
        :param l1: linked list head node
        :param l2: linked list head node
        :return: ListNode
        """
        
#         carry = 0
#         # dummy head
#         head = curr = ListNode(0)
#         while l1 or l2:
#             val = carry
#             if l1:
#                 val += l1.val
#                 l1 = l1.next
#             if l2:
#                 val += l2.val
#                 l2 = l2.next
#             curr.next = ListNode(val % 10)
#             curr = curr.next
#             carry = val / 10
#         if carry > 0:
#             curr.next = ListNode(carry)
        
#         return head.next

    
        result_head = ListNode(0) #initialize a new list to store the result
        
        cur1 = l1
        cur2 = l2
        cur = result_head
        while cur1 or cur2:
            cur.val = cur.val + self.addNode(cur1, cur2)
            
            if cur.val < 10:
                if cur1 and cur1.next or cur2 and cur2.next: #next node
                    cur.next = ListNode(0)
            else:
                cur.val -= 10
                cur.next = ListNode(1) #initialze result list node plus one
                
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
            cur = cur.next
            
        return result_head
   



    def addNode(self, node1, node2):
        """
        Handles None situation
        :param node1: ListNode
        :param node2: ListNode
        :return: integer, summation
        """
        if not node1 and not node2:
            raise Exception("Two nodes are none")
        if not node1:
            return node2.val
        if not node2 :
            return node1.val
        return node1.val + node2.val
        
    
        
            