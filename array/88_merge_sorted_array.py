#088_merge_sorted_array
#link: https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

# -----solution-----
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not nums1: 
            return nums2
        if not nums2:
            return nums1
        
        i = m-1
        j = n-1
        k = m+n-1
        
        # compare the vlaue from the end of lists 
        # insert the value from the end of list nums1 
        
        while i>=0 and j>=0: 
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            elif nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        while i>= 0:
            nums1[k] = nums1[i]
            i-=1
            k-=1
        while j>= 0:
            nums1[k] = nums2[j]
            j-=1
            k-=1

        return nums1
    
# -----test case-----
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

s = Solution()
print(s.merge(nums1, m, nums2, n))