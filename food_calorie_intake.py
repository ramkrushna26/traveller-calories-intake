

class Heap:	
    def __init__(self):
        self.heap = [None]
    
    def generate_heap(self, items):
        for item in items:
            self.heap.append(item)

    def is_root(self, item):
        return self.heap[1] == item
        
    def get_child(self, item):
        children = []
        
    def is_child(self, item):
        return self.root
    
    def get_heap(self):
        return list(self.heap)
        
    def get_size(self):
        return (len(self.heap) - 1)
        
    def max_heapify(self, index):
        left = (index * 2)
        right = self.get_size() > (index * 2) and ((index * 2) + 1) or 0
        #print("index=>{}, left=>{}, right=>{}".format(index, left, right))
        #print("index=>{}, left=>{}, right=>{}".format(self.heap[index], self.heap[left], self.heap[right]))
        if left <= self.get_size() and self.heap[left][2] > self.heap[index][2]:
            largest = left
        else:
            largest = index
        if right != 0:
            if right <= self.get_size() and self.heap[right][2] > self.heap[largest][2]:
                largest = right
        if largest != index:
            temp = self.heap[index]
            self.heap[index] = self.heap[largest]
            self.heap[largest] = temp
        #print("current_heap=> ", self.get_heap())
        if (index // 2) > 0:
            self.max_heapify(index - 1)

if __name__ == '__main__':
    infile = "inputsPS16Q2.txt"
    elements = []
    
    with open(infile, "r") as f:
        _, no_of_food_items = f.readline().split(":")
        _, max_bag_weight = f.readline().split(":")
        
        line = f.readline()
        while(line):
            food_item, quantity, calories = line.split("/")
            elements.append((food_item.strip(), int(quantity), int(calories)))
            if len(elements) == no_of_food_items:
                print("Ignore Food Items greater that {}".format(no_of_food_items))
                break
            line = f.readline()
         
    heap = Heap()
    heap.generate_heap(elements)
    heap_size = heap.get_size()
    loop_len = (heap_size // 2)
    
    while (loop_len > 0):
        heap.max_heapify(heap_size // 2)
        loop_len -= 1
    
    print(heap.get_heap())
    

    
