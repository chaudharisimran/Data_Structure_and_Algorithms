"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""
def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if len(nums)<1:
            return nums
        
        # Approch 1  O(n)
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == 0 and nums[j] !=0:
                # swap
                nums[i] = nums[j]
                nums[j] = 0
                i += 1
                j +=1
            elif nums[i] == 0 and nums[j] == 0:
                j = j+1
            else:
                i +=1
                j +=1
        return nums


        # Approch 2 O(n2)

        for i in range(len(nums) - 1):
            if nums[i] == 0:
                # serach and swap
                for j in range(i+1, len(nums)):
                    if nums[j] !=0:
                        break
                nums[i] = nums[j]
                nums[j] = 0
        return nums
            
        
        
                



        
