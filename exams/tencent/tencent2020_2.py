'''

INTERVIEW - 2.1

求两个链表的交点
如果两个链表相交，返回交点，否则返回 null

Example 1：交点为8
listA = [2,1,8,4,5]
listB = [3,0,6,8,4,5]

Example 2: 返回 null
listA = [2,6,4]
listB = [1,5]

注意：不可以改变两个链表的结构
提示：链表等长 / 协同遍历

'''


class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkedList(object):
    def __init__(self):
        self.head = None
    
    def get_length(self):
        cur = self.head
        length = 0
        while cur is not None:
            length += 1
            cur = cur.next
        return length
    
    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
    
    def drop_top(self, diff):
        cur = self.head
        while cur.next is not None and diff > 0:
            diff -= 1
            cur = cur.next
        self.head = cur


def check_intersect(listA, listB):
    # get length of both linked lists
    lengthA = listA.get_length()
    lengthB = listB.get_length()
    print("length of two lists", listA.get_length(), listB.get_length())
    print("head of two lists", listA.head.item, listB.head.item)

    # drop top N elements
    listA.drop_top(lengthA - lengthB)
    listB.drop_top(lengthB - lengthA)
    print("length of two lists", listA.get_length(), listB.get_length())
    print("head of two lists", listA.head.item, listB.head.item)

    res = None
    while listA.head.next is not None and \
        listB.head.next is not None:
        # start of intersection
        if listA.head.item == listB.head.item and \
            res is None:
            res = listA.head.item
        # not equal then reset the start
        elif listA.head.item != listB.head.item and \
            res is not None:
            res = None
        # iterate two linked lists
        listA.head = listA.head.next
        listB.head = listB.head.next

    return res


if __name__ == "__main__":
    listA = SingleLinkedList()
    listB = SingleLinkedList()
    for ii in [2,1,8,4,5,4]:
        listA.append(ii)
    for jj in [3,0,6,8,4,5,4]:
        listB.append(jj)
    print(check_intersect(listA, listB))