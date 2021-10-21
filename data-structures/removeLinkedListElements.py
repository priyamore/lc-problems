'''
Problem Statement:
Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, and return the new head.
Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
'''

#Solution 1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        #linked list with no elements 
        if temp is None:
            return temp
        
        #linked list with single element
        elif temp.next is None:
            if temp.val == val:
                temp = temp.next
            return temp
            #else keep the pointer where it is
        
        #if the first element of the remaining linked list matches
        while temp and temp.val == val:
            temp = temp.next
        
        #need the reference later to return
        res = temp
        
        while temp and temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return res