"""
Problem Statement: Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000

"""
def threeConsecutiveOdds(arr):
        count = 0
        N = len(arr) - 2

        for i in range(N):
            j = i+3
            subarray = arr[i:j]
            for k in range(len(subarray)):
                if subarray[k] % 2 !=0 :
                    count = count + 1
            
            if count == 3:
                print("True")
                return True
            else:
                count = 0

        return False
        
    
## Test Solution
input_list = [1,2,34,3,4,5,7,23,12]
threeConsecutiveOdds(input_list)
    
## Test 2
# arr = [2,6,4,1]
# threeConsecutiveOdds(arr)
