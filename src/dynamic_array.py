class DynamicArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity

    def insert(self, index, value):

        # make sure we open space
        if self.count >= self.capacity:
            # TODO: Make array dynamically resize
            print("ERROR: Array is full!")
            return

        # make sure index is in range
        if index > self.count:
            print("Error: Index out of range")
            return

        # shift everything over to right
        # Start with the last one move it to the right
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

        # insert our value
        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(self.count, value)


my_array = DynamicArray(4)
my_array.insert(0, 1)
my_array.insert(0, 2)
my_array.insert(1, 3)
my_array.insert(3, 4)
my_array.insert(0, 5)
print(my_array.storage)
