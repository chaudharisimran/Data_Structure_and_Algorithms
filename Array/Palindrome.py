"""
Problem Statement : Given an integer x, return true if x is a 
palindrome and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
"""

## Solution 1 
## Approach : Reverse the number and check if original number and reverse number is same
def check_palindrome(x):
    original_number = x
    reverse_num = 0
    while(x > 0):
        remainder = x%10
        reverse_num = reverse_num * 10 + remainder
        x = x // 10
    if reverse_num == original_number:
        print(True)
        return True 
    print(False)
    return False


## Solution 2 
## Convert number to string and keep checking characters from start and end
def checkPalindrome(x):
    num_str = str(x)
    start = 0
    end = len(num_str) - 1
    while start < end:
        if num_str[start] != num_str[end]:
            print(False)
            return
        start += 1
        end -= 1


## Test Solution 
x = -121
check_palindrome(x)
checkPalindrome(x)


