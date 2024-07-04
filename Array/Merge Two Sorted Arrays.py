"""
Problem Statement : Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

## Approach 1 
def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        pointer1 = 0
        pointer2 = 0
        num1_len = len(nums1)
        num2_len = len(nums2)
        merged_array = []

        while pointer1 < num1_len and pointer2 < num2_len:
            if nums1[pointer1] < nums2[pointer2]:
                merged_array.append(nums1[pointer1])
                pointer1 += 1
            else:
                merged_array.append(nums2[pointer2])
                pointer2 += 1

        # If any elements are left after one of the list exhausts in above while loop append them at end
        while pointer1 < num1_len:
            merged_array.append(nums1[pointer1])
            pointer1 += 1

        while pointer2 < num2_len:
            merged_array.append(nums2[pointer2])
            pointer2 += 1

        print(merged_array)
        
        merge_array_len = len(merged_array)
        if merge_array_len % 2 == 0 :
            # even
            val1 = merge_array_len//2 
            val2 = (merge_array_len-1)//2
            median = (merged_array[val1] + merged_array[val2]) / 2.0
            print(median)
            return median

        else:
            # odd 
            median = merged_array[(merge_array_len-1)//2]
            print(median)
            return median
    
# Test Solution
nums1 = [1,3]
nums2 = [2]
findMedianSortedArrays(nums1,nums2)

nums1 = [1,2]
nums2 = [3,4]
findMedianSortedArrays(nums1,nums2)
