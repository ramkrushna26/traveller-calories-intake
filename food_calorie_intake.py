

from os.path import exists

class Heap:	
    def __init__(self, items):
        self.heap = [None]
        self.generate_heap(items)
    
    #Generate the initial from given list
    def generate_heap(self, items):
        for item in items:
            self.heap.append(item)

    def get_root(self):
        return self.heap[1]
    
    def get_heap(self):
        return list(self.heap)
        
    def get_size(self):
        return len(self.heap) - 1
    
    #Remove the root element from list and max heapify it
    def remove_root(self):
        last_child = self.heap.pop()
        self.heap[1] = last_child
        self.wrap_max_heapify()
    
    #Modify the heap items as per values specified
    def modify_root(self, food_item, quantity, calories):
        del self.heap[1]
        self.heap.insert(1,(food_item, quantity, calories))
    
    #Generates the max heap
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

    def wrap_max_heapify(self):
        heap_size = self.get_size()
        loop_len = (heap_size // 2)
        while (loop_len > 0):
            self.max_heapify(heap_size // 2)
            loop_len -= 1


if __name__ == '__main__':
    if exists("inputsPS16Q2.txt"):
        infile = "inputsPS16Q2.txt"
    elif exists("promptsPS16Q2.txt"):
        infile = "promptsPS16Q2.txt"
    else:
        raise Exception("Input File Not Found!")
    elements = []
    current_bag_weight = 0
    total_calories = 0
    items_to_carry = {}
    
    #Reading the input file
    with open(infile, "r") as f:
        _, no_of_food_items = f.readline().split(":")
        _, max_bag_weight = f.readline().split(":")
        no_of_food_items = int(no_of_food_items)
        max_bag_weight = int(max_bag_weight)
        
        line = f.readline()
        while(line):
            food_item, quantity, calories = line.split("/")
            elements.append((food_item.strip(), int(quantity), int(calories)))
            items_to_carry[food_item.strip()] = 0
            if len(elements) > no_of_food_items:
                print("Ignore Food Items greater than {} provided.".format(no_of_food_items))
                break
            line = f.readline()

    #Generating heap from provided food items
    heap = Heap(elements)
    #Max heapigfying the heap
    heap.wrap_max_heapify()
    
    #Processing for calculating item to carry along with total calories
    while(True):
        if current_bag_weight == max_bag_weight:
            break
        root = heap.get_root()
        if root[1] < (max_bag_weight - current_bag_weight):
            current_bag_weight += root[1]
            total_calories += (root[1] * root[2])
            items_to_carry.update({root[0]: 1 })
            heap.remove_root()
        else:
            remain_quantity = max_bag_weight - current_bag_weight
            current_bag_weight += remain_quantity
            total_calories += (remain_quantity * root[2])
            items_to_carry.update({root[0]: remain_quantity / root[1] })
            heap.modify_root(root[0], root[1] - remain_quantity, calories)
    
    outfile = open("outputPS16Q2.txt", "a")
    outfile.write("Total Calories: {}\n".format(total_calories))
    outfile.write("Food Item Selection Ratio: \n")
    for food_item, ratio in items_to_carry.items():
        outfile.write("{}: {}\n".format(food_item, ratio))
    outfile.close()
    
    
