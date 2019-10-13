class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class SingleCycleLinkedList(object):
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def get_length(self):
        if self.is_empty():
            return 0
        length = 1
        cur = self.head
        while cur.next != self.head:
            length += 1
            cur = cur.next
        return length
    
    def iterate(self):
        if self.is_empty():
            return
        cur = self.head
        while cur.next != self.head:
            yield cur.item
            cur = cur.next
        yield cur.item
    
    def prepend(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            node.next = self.head
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
        self.head = node
    
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head
    
    def insert(self, index, item):
        if index <= 0:
            self.prepend(item)
        elif index > (self.get_length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node
    
    def remove(self, item):
        if self.is_empty():
            return
        cur = self.head
        pre = None
        # remove first element
        if cur.item == item:
            if cur.next != self.head:
                while cur.next != self.head:
                    cur = cur.next
                cur.next = self.head.next
                self.head = self.head.next
            else:
                self.head = None
        # not first element
        else:
            pre = self.head
            while cur.next != self.head:
                if cur.item == item:
                    pre.next = cur.next
                    return True
                else:
                    pre = cur
                    cur = cur.next
        # remove last element
        if cur.item == item:
            pre.next = self.head
            return True
        return False
    
    def find(self, item):
        return item in self.iterate()
    
    def display(self):
        if self.is_empty():
            return
        cur = self.head
        while cur.next != self.head:
            print(cur.item, ' ->', end=' ')
            cur = cur.next
        print(cur.item, ' -> ', self.head.item)


if __name__ == '__main__':
    link_list = SingleCycleLinkedList()
    for i in range(10):
        link_list.append(i)
    link_list.display()
    link_list.prepend(11)
    link_list.display()
    link_list.remove(1)
    link_list.display()
    link_list.insert(7, 100)
    link_list.display()
    print(link_list.find(8))
