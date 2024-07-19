"""
Problem Statement : Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 105.
All elements in the matrix are distinct.
"""

## Approach 1
class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        min_values_in_row = []
        min_value_in_row_index = []

        n = len(matrix)
        for j in range(n):
            min_value = min(matrix[j])
            min_values_in_row.append(min_value)
            row_length = len(matrix[j])
            for i in range(row_length):
                if min_value == matrix[j][i]:
                    min_index = i
                    min_value_in_row_index.append(i)
                    

        print(min_values_in_row)
        print(min_value_in_row_index)


        count = 0
        for h in min_value_in_row_index:
            max_element = matrix[0][h]
            for k in range(n):
                # print(matrix[k][h])
                if matrix[k][h] > max_element:
                    max_element = matrix[k][h]
            
            # print(max_element)
            if max_element == min_values_in_row[count]:
                return [max_element]
                
            count = count + 1




    

        
