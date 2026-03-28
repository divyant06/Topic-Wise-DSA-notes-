class DynamicArray:
    def __init__(self):
        self.data = [0] * 1   # initial capacity = 1
        self.size = 0
        self.capacity = 1

    def append(self, value):
        # if array is full, increase size
        if self.size == self.capacity:
            self.resize()

        self.data[self.size] = value
        self.size += 1
        print("Added:", value, " Size:", self.size, " Capacity:", self.capacity)

    def resize(self):
        new_capacity = self.capacity * 2
        new_data = [0] * new_capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity
        print("Resized to capacity:", self.capacity)

    def pop(self):
        if self.size == 0:
            print("Array is empty")
            return

        removed = self.data[self.size - 1]
        self.size -= 1
        print("Removed:", removed, " Size:", self.size, " Capacity:", self.capacity)


# main
arr = DynamicArray()

arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)

arr.pop()
arr.pop()