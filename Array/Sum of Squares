### <span style='color:yellow'>**Problem Statement**</span>

**Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.**

**Example 1:**
- Input: c = 5
- Output: true
- Explanation: 1 * 1 + 2 * 2 = 5

**Example 2:**
- Input: c = 3
- Output: false

**Constraints:**
- 0 <= c <= 231 - 1

#--------------------------------------------------------------------------------------------------------#
### <span style='color:yellow'>**Solving Approach**</span>

To solve this problem, we can use the two-pointer technique. The idea is to check if there exist two integers 𝑎 and 𝑏 such that 𝑎2 + 𝑏2 = 𝑐. We'll start with 𝑎=0 and b at the largest possible value such that 𝑏2 is less than or equal to c.

**Here's the step-by-step approach:**

- Initialize two pointers: a starting from 0 and b starting from the integer part of the square root of c.
- While a is less than or equal to b, calculate 𝑎2 + 𝑏2
- If 𝑎2 + 𝑏2 equals c return true.
- If 𝑎2 + 𝑏2 is less than c, increment a.
- If 𝑎2 + 𝑏2 is greater than c, decrement b.
- If the loop exits without finding such a and b, return false.
#--------------------------------------------------------------------------------------------------------#
import math

def sum_of_squares(c):
    a = 0
    b = int(math.sqrt(c))
    while a <= b:
        current_sum_of_square = a**2 + b**2
        if current_sum_of_square == c:
            return True
        elif current_sum_of_square < c:
            a = a+1
        elif current_sum_of_square > c:
            b = b-1
    return False

## Test Solution
c= 5
result = sum_of_squares(c)
print(result)
