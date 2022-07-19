class Node:
    def __init__(self, rect, color, next):
        self.color = color
        self.rect = rect
        self.visible = True
        self.next = next


class Briks:
    def __init__(self):
        self.head = None

    def push_front(self, rect, color):
        if self.head is None:
            self.head = Node(rect, color, None)
        else:
            self.head = Node(rect, color, self.head)

    def size(self):
        size = 0
        tmp = self.head
        while tmp != None:
            size += 1
            tmp = tmp.next
        return size

    def size_visible(self):
        size = 0
        tmp = self.head
        while tmp != None:
            if tmp.visible:
                size += 1
            tmp = tmp.next
        return size
