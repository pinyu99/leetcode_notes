#021 merge two sorted lists
#link: https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150

# -----solution-----

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy_head = ListNode() # create dummy head as a node 
        curr = dummy_head  # as a pointer

        if not list1 :
            return list2
        if not list2:
            return list1
        
        while list1 and list2: # going to iterate two lists
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next #update list1 pointer 
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next # update the curr pointer

        # if one of these two lists is non-null
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return dummy_head.next


