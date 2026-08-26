class ListNode:
    def __init__(self, val:int, node:ListNode = None):
        self.val = val
        self.next_node = node

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr_node = self.head
        while(curr_node):
            if index == 0:
                return curr_node.val
            index -= 1
            curr_node = curr_node.next_node
        return -1

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val, self.head)
        self.head = new_head
        if self.tail is None:
            self.tail = self.head
        

    def insertTail(self, val: int) -> None:
        new_tail = ListNode(val)
        if self.tail:
            self.tail.next_node = new_tail
        self.tail = new_tail
        if self.head is None:
            self.head = self.tail

    def remove(self, index: int) -> bool:
        curr_node = self.head
        prev_node = None
        while(curr_node):
            if not index:
                if prev_node:
                    prev_node.next_node = curr_node.next_node
                if self.head == curr_node:
                    self.head = curr_node.next_node
                if self.tail == curr_node:
                    self.tail = prev_node 
                return True
            prev_node = curr_node
            curr_node = curr_node.next_node
            index -= 1
        return False
        

    def getValues(self) -> List[int]:
        curr_node = self.head
        arr = []
        while(curr_node):
            arr.append(curr_node.val)
            curr_node = curr_node.next_node
        return arr
        
