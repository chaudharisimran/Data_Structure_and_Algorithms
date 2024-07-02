"""
Problem Statement : Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 """

def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # # Approach 1 : Using HashMap
        hashMap = {}
        intersect = []

        for i in range(len(nums1)):
            if nums1[i] in hashMap:
                hashMap[nums1[i]] = hashMap[nums1[i]] + 1
            else:
                hashMap[nums1[i]] = 1
        
        # Scan second Array
        for i in range(len(nums2)):
            if nums2[i] in hashMap and hashMap[nums2[i]] >0:
                hashMap[nums2[i]] = hashMap[nums2[i]] -1
                intersect.append(nums2[i])

        return intersect

        

        




        
