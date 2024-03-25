class CircularBuffer:
    def __init__(self, max_size):
        self.max_size = max_size
        self.buffer = []

    def add(self, item):
        self.buffer.append(item)
        if len(self.buffer) > self.max_size:
            self.buffer.pop(0)

    def __getitem__(self, index):
        return self.buffer[index]

    def __len__(self):
        return len(self.buffer)
    

buffer = CircularBuffer(3)
print(len(buffer))  # 0

buffer.add('a')
buffer.add('b')
buffer.add('c')
print(len(buffer))  # 3

print(buffer[0])  # 'a'
print(buffer[1])  # 'b'
print(buffer[2])  # 'c'

buffer.add('d')
print(len(buffer))  # 3
print([buffer[0], buffer[1], buffer[2]])  # ['b', 'c', 'd']

buffer.add('e')
print(len(buffer))  # 3
print([buffer[0], buffer[1], buffer[2]])