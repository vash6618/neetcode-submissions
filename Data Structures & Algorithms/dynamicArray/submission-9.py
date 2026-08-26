class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * self.capacity
        self.num_ele = 0


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.num_ele + 1 > self.capacity:
            self.resize()
        print(n, self.num_ele, self.capacity, len(self.arr))
        self.arr[self.num_ele] = n
        self.num_ele += 1



    def popback(self) -> int:
        num = self.arr[self.num_ele - 1]
        self.num_ele -= 1
        return num
 

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [None]*self.capacity
        for i in range(self.num_ele):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.num_ele
        
    
    def getCapacity(self) -> int:
        return self.capacity
