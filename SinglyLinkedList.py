class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value, None)
        else:
            self.head = Node(value, self.head)

    def append(self, value):
        if self.head is None:
            self.head = Node(value, None)
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = Node(value, None)

    def set_head(self, index):
        cur_node = self.head
        
        for _ in range(index):
            cur_node = cur_node.next
        self.head = cur_node

    def access(self, index):
        cur_node = self.head
        
        for _ in range(index):
            cur_node = cur_node.next
        
        return cur_node.value

    def insert(self, index, value):
        cur_node = self.head
        
        for _ in range(index-1):
            cur_node = cur_node.next
        
        prev_next_node = cur_node.next
        cur_node.next = Node(value, prev_next_node)

    def remove(self, index):
        cur_node = self.head
        
        for _ in range(index):
            cur_node = cur_node.next
        prev_next_node = cur_node.next
        cur_node = self.head
        
        for _ in range(index-1):
            cur_node = cur_node.next
        cur_node.next = prev_next_node

    def print(self):
        cur_node = self.head
        while cur_node.next is not None:
            print(cur_node.value, end=' ')
            cur_node = cur_node.next
        print(cur_node.value, end=' ')
        print()

my_list = SinglyLinkedList()

for i in range(10):
    my_list.append(i + 1)

my_list.print()

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