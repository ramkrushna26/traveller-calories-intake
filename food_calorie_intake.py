

class Heap:	
    def __init__(self, items):
        self.heap = items

    def is_root(self, item):
        return self.heap[1] == item
        
    def get_child(self, item):
        children = []
        
    def is_child(self, item):
        return self.root
    
    def get_heap(self):
        return self.heap
        
    def get_size(self):
        return len(self.heap)
        
    def max_heapify(self, index):
        left = index * 2
        right = (index * 2) + 1
        if left <= self.get_size() and self.heap[left] > self.heap[index]:
            largest = left
        else:
            largest = right
        if right <= self.get_size() and self.heap[right] > self.heap[index]:
            largest = right
        if largest != index:
            temp = self.heap[index]
            self.heap[index] = self.heap[largest]
            self.heap[largest] = temp
            self.max_heapify(largest)

if __name__ == '__main__':
    infile = "inputsPS16Q2.txt"
    elements = [None]
    
    with open(infile, "r") as f:
        _, no_of_food_items = f.readline().split(":")
        _, max_bag_weight = f.readline().split(":")
        
        line = f.readline()
        while(line):
            food_item, quantity, calories = line.split("/")
            elements.append((food_item, int(quantity), int(calories)))
            if len(elements) == no_of_food_items:
                print("Ignore Food Items greater that {}".format(no_of_food_items))
                break
            line = f.readline()
         
    heap = Heap(elements)
    heap_size = heap.get_size()
    loop_len = heap_size // 2
    while (loop_len > 0):
        heap.max_heapify(loop_len)
        loop_len -= 1
    
    print(heap.get_heap())
    
