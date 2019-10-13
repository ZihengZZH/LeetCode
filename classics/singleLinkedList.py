class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class SingleLinkedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def get_length(self):
        cur = self.head
        length = 0
        while cur is not None:
            length += 1
            cur = cur.next
        return length
    
    def iterate(self):
        cur = self.head
        while cur is not None:
            yield cur.item
            cur = cur.next

    def prepend(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
    
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
    
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
        cur = self.head
        pre = None
        while cur is not None:
            if cur.item == item:
                if not pre:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next
        return False

    def find(self, item):
        return item in self.iterate()
    
    def display(self):
        cur = self.head
        while cur is not None:
            if cur.next is not None:
                print(cur.item, ' ->', end=' ')
            else:
                print(cur.item)
            cur = cur.next


if __name__ == '__main__':
    link_list = SingleLinkedList()
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
