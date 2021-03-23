import array

class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('l', [0]*capacity)
    
    def is_empty(self):
        return self.length == 0

    def prepend(self, value):
        if self.capacity == self.length:
            self.capacity *= 2
            new_array = array.array('l', [0]*self.capacity)
            for i in range(self.length):
                new_array[i+1] = self.array[i]
            self.array = new_array
        else:
            for i in range(self.length-1, -1, -1):
                self.array[i+1] = self.array[i]
        
        self.array[0] = value
        self.length += 1

    def append(self, value):
        if self.capacity == self.length:
            self.capacity *= 2
            new_array = array.array('l', [0]*self.capacity)
            for i in range(self.length):
                new_array[i] = self.array[i]
            self.array = new_array
        
        self.array[self.length] = value
        self.length += 1

    def set_head(self, index):
        self.array = self.array[index:]
        self.capacity -= index
        self.length -= index

    def access(self, index):
        return self.array[index]

    def insert(self, index, value):
        if self.capacity == self.length:
            self.capacity *= 2
            new_array = array.array('l', [0]*self.capacity)
            for i in range(index, self.length):
                new_array[i+1] = self.array[i]
            for i in range(index):
                new_array[i] = self.array[i]
            self.array = new_array
        else:
            for i in range(self.length - 1, index - 1, -1):
                self.array[i + 1] = self.array[i]

        self.array[index] = value
        self.length += 1

    def remove(self, index):
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        self.length -= 1

    def print(self):
        print(self.array.tolist()[:self.length])

my_list = ArrayList(4)
my_list.print()

for i in range(6):
    my_list.append(i)
my_list.print()

# 소스 코드를 보고 이해하고 다시 작성하는 방식으로 진행했는데 소스 코드에서 length와 capacity가 동일한 상황에 
# insert함수를 호출하면 해당 index이전의 데이터를 새로운 array에 저장하는 코드가 없어 수정했습니다.

my_list.insert(2, 3)
my_list.print()