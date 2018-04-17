'''

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''

from math import ceil, floor

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def display(self):
        while self.next:
            print(self.val, end=" ")
            self = self.next
        print(self.val, end="\n")


class Solution:
    def list2num(self, lst):
        num,ord = 0,0
        while lst.next:
            num += lst.val * pow(10,ord)
            lst = lst.next
            ord += 1
        num += lst.val * pow(10,ord)
        return num

    def num2list(self, num):
        lst, lst_links = [], []
        while num / 10 != 0:
            lst.append(num%10)
            lst_links.append(ListNode(num%10))
            num = int(num/10)
        lst_links.append(ListNode(num%10))
        for i in range(len(lst)-1):
            lst_links[i].next = lst_links[i+1]
        return lst_links[0]

    # troublesome when handling large numbers 
    # Complexity O(4n) (4 loops time-consuming)
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.list2num(l1)
        num2 = self.list2num(l2)
        sum3 = num1 + num2
        #print(sum3)
        return self.num2list(sum3)
    
    # Complexity O(n)
    def addTwoNumbers_online(self, l1, l2):
        carry = 0
        root = nxt = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            nxt.next = ListNode(val) # init at next
            nxt = nxt.next # move forward
        return root.next

    '''
    divmod()
    Take two (non complex) numbers as arguments and return a pair of numbers consisting of 
    their quotient and remainder when using long division. With mixed operand types, 
    the rules for binary arithmetic operators apply. 
    '''


if __name__ == "__main__":
    l1_1 = ListNode(1)
    l1_2 = ListNode(7)
    l1_3 = ListNode(1)
    l1_1.next = l1_2
    l1_2.next = l1_3
    l2_1 = ListNode(5)
    l2_2 = ListNode(6)
    l2_3 = ListNode(9)
    l2_1.next = l2_2
    l2_2.next = l2_3
    l1_1.display()
    l2_1.display()

    solu = Solution()
    res = solu.addTwoNumbers_online(l1_1,l2_1)
    res.display()

        