"""
Problem Statement:You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Solution 1 
def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None and list2 == None:
            return None
        if list1 == None and list2 !=None:
            return list2
        if list2 == None and list1 != None:
            return list1

        new_head = ListNode()
        curr = new_head
        
        while(list1 and list2):
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                curr = curr.next
                list2 = list2.next
        
        # append the remaining elements
        if list1 == None and list2 != None:
            while list2:
                curr.next = ListNode(list2.val)
                curr = curr.next
                list2 = list2.next
        if list1 != None and list2 == None:
            while list1:
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next


        return new_head.next

        
