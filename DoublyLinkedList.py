class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        return self.head is None

    def prepend(self, value):
        node = Node(value, self.head, None)
        self.head.prev = node
        self.head = node

    def append(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head

        else:
            node = Node(value, None, self.tail)
            self.tail.next = node
            self.tail = node

    def set_head(self, index):
        cur_node = self.head
        for _ in range(index):
            cur_node = cur_node.next
        cur_node = self.head
        cur_node.prev = None

    def access(self, index):
        cur_node = self.head
        for _ in range(index):
            cur_node = cur_node.next
        return cur_node.value

    def insert(self, index, value):
        prev_node = self.head
        next_node = self.head

        for _ in range(index-1):
            prev_node = prev_node.next
        
        for _ in range(index):
            next_node = next_node.next

        node =  Node(value, next_node, prev_node)
        prev_node.next =  node
        next_node.prev = node

    def remove(self, index):
        prev_node = self.head
        next_node = self.head

        for _ in range(index-1):
            prev_node = prev_node.next
        
        for _ in range(index+1):
            next_node = next_node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node


    def print(self):
        cur_node = self.head
        while cur_node.next is not None:
            print(cur_node.value, end=' ')
            cur_node = cur_node.next
        print(cur_node.value, end=' ')
        print()

    def rev_print(self):
        cur_node = self.tail
        while cur_node.prev is not None:
            print(cur_node.value, end=' ')
            cur_node = cur_node.prev
        print(cur_node.value, end=' ')    
        print()

my_list = DoublyLinkedList()

for i in range(10):
    my_list.append(i + 1)

my_list.print()
my_list.rev_print()

for i in range(10):
    my_list.prepend(i + 1)

my_list.print()

value = my_list.access(3)
print('my_list.access(3) = ' + str(value))

my_list.insert(8, 128)
my_list.print()

my_list.remove(4)
my_list.print()

my_list.set_head(10)
my_list.print()

my_list.rev_print()