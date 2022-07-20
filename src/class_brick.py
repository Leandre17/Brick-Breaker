from typing import Tuple, Any
from pygame import Rect


class Node:
    def __init__(
        self: Any, rect: Rect, color: Tuple[int, int, int], next: Any
    ) -> (None):
        self.color: Tuple[int, int, int] = color
        self.rect: Rect = rect
        self.visible: bool = True
        self.next: Node = next


class Briks:
    def __init__(self: Any) -> (None):
        self.head: Node = None

    def push_front(self: Any, rect: Rect, color: Tuple[int, int, int]) -> (None):
        if self.head is None:
            self.head = Node(rect, color, None)
        else:
            self.head = Node(rect, color, self.head)

    def size(self: Any) -> (int):
        size: int = 0
        tmp: Node = self.head
        while tmp != None:
            size += 1
            tmp = tmp.next
        return size

    def size_visible(self: Any) -> (int):
        size: int = 0
        tmp: Node = self.head
        while tmp != None:
            if tmp.visible:
                size += 1
            tmp = tmp.next
        return size
