#148 sort list
#link: https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy_head = ListNode()
        curr = dummy_head

        for i in head: 
            

# test case 
head = [4,2,1,3] #input
# head = [1,2,3,4] #output
        