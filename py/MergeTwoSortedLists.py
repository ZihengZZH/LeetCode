'''

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        # temporary head
        head = sorted_list = ListNode(0)
        # when l1 and l2 both not None
        while l1 and l2:
            # l1 value less than l2 value
            if l1.val < l2.val:
                # temporary head to l1
                sorted_list.next = l1
                # l1 iterates
                l1 = l1.next
            # l1 value greater than l2 value
            else:
                # temporary head to l2
                sorted_list.next = l2
                # l2 iterates
                l2 = l2.next
            # sorted_list iterates
            sorted_list = sorted_list.next
        # this lines considers scenarios
        # 1. l1 or l2 is None
        # 2. end of iteration when l1 or l2 is None
        sorted_list.next = l1 or l2
        # return full merged linked list
        return head.next
