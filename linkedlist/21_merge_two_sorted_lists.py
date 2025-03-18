#021 merge two sorted lists
#link: https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150

# -----solution-----

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# iteration 
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


# recursive
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        
# test case 
# list1 = [1,3,5] 
# list2 = [2,4,6]

# (第一輪)
# mergetwolist(1->3->5, 2->4->6)
# 1 < 2 所以 1 作為head
# 1.next = mergetwolist (3->5, 2->4->6)

# (第二輪)
# mergetwolist(3->5, 2->4->6)
# 2 < 3 所以 2 作為head
# 2.next = mergetwolist (3->5, 4->6)

# (第三輪)
# mergetwolist(3->5, 4->6)
# 3 < 4 所以 3 作為head
# 3.next = mergetwolist (5, 4->6)

# (第四輪)
# mergetwolist(5, 4->6)
# 4 < 5 所以 4 作為head
# 4.next = mergetwolist (5, 6)

# (第五輪)
# mergetwolist(5, 6)
# 5 < 6 所以 5 作為head
# 5.next = mergetwolist (none, 6)

# (第六輪)
# mergetwolist (none, 6)
# list1 is none
# return list2 (equal to 6)