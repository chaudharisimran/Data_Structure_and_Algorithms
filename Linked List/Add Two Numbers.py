"""
Problem Statement :  You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]


Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

 """

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        current = head
        carry = 0
        while (l1 is not None or l2 is not None):
            value1 = 0
            value2 = 0

            if l1 is not None:
                value1 = l1.val
                l1 = l1.next
            
            if l2 is not None:
                value2 = l2.val
                l2 = l2.next

            sum_of_nodes = value1 + value2 + carry
            carry = sum_of_nodes // 10
            new_node_value = sum_of_nodes % 10

            ## add the value as new node in result list
            current.next =  ListNode(new_node_value)
            current = current.next
        
        ## If any carry value is left after summation of all digits add carry value as a node
        if carry > 0:
            current.next =  ListNode(carry)
            current = current.next

        return head.next


