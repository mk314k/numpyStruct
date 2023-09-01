import numpy as np

class npList:
    def __init__(self, object_type = object, capacity = 10):
        self.__capacity = capacity
        self.__size = 0
        self.__data = np.empty(capacity, dtype=object_type)

    @property
    def size(self):
        return self.__size
    
    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.__data[index]
        raise IndexError("Index out of range")

    def append(self, value):
        if self.size == self.__capacity:
            self._resize(self.__capacity * 2)
        self.__data[self.size] = value
        self.__size += 1

    def _resize(self, new_capacity):
        new_array = np.empty(new_capacity, dtype=object)
        new_array[:self.size] = self.__data
        self.__data = new_array
        self.__capacity = new_capacity

    def __repr__(self):
        elements = ', '.join(str(self.__data[i]) for i in range(self.size))
        return f"npList([{elements}])"
