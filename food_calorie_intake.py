

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
        if self.get_size() > 0:
            return self.heap[1]
        else:
            return None 
    
    def get_heap(self):
        if self.get_size() == 0:
            return None
        else:
            return list(self.heap)
        
    def get_size(self):
        if len(self.heap) == 1:
            return 0
        else:
            return len(self.heap) - 1
    
    #Remove the root element from list and max heapify it
    def remove_root(self):
        last_child = self.heap.pop()
        self.heap[1] = last_child
        if self.get_size() > 1:
            self.wrap_max_heapify()
    
    #Modify the heap items as per values specified
    def modify_root(self, food_item, quantity, calories):
        del self.heap[1]
        self.heap.insert(1,[food_item, quantity, calories])
    
    #Getting the left child of index passed if left is present
    def left_child(self, index):
        return (2 * index) <= self.get_size() and (index * 2) or None
    
    #Getting the right child of index passed if right is present    
    def right_child(self, index):
        return (2 * index + 1) <= self.get_size() and (index * 2 + 1) or None
    
    #Generates the max heap
    def max_heapify(self, index):
        left = self.left_child(index)
        right = self.right_child(index)
        #print("index=>{}, left=>{}, right=>{}".format(index, left, right))
        #print("index=>{}, left=>{}, right=>{}".format(self.heap[index], self.heap[left], self.heap[right]))
        if left != None and left <= self.get_size() and self.heap[left][2] > self.heap[index][2]:
            largest = left
        else:
            largest = index
        if right != None:
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
        try:
            no_of_food_items = int(no_of_food_items)
            max_bag_weight = int(max_bag_weight)
        except ValueError:
            raise Exception("Incorrect input provided instead of INT. Please check input file!")
        line = f.readline()
        while(line):
            food_item, quantity, calories = line.split("/")
            try:
                elements.append([food_item.strip(), int(quantity), int(calories)])
            except ValueError:
                raise Exception("Couldn't Understand food items in input file. Please check input file!")
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
    root = heap.get_root()
    if root == None:
        raise Exception("Didn't provided any food items.")
    elif root[1] > max_bag_weight:
        raise Exception("No Food Items to carry with given bag weight")

    while(True):
        root = heap.get_root()
        if current_bag_weight == max_bag_weight:
            break
        elif root[1] < (max_bag_weight - current_bag_weight):
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
        if heap.get_size() == 0:
            break
    
    outfile = open("outputPS16Q2.txt", "a")
    outfile.write("Total Calories: {}\n".format(total_calories))
    outfile.write("Food Item Selection Ratio: \n")
    for food_item, ratio in items_to_carry.items():
        outfile.write("{}: {}\n".format(food_item, ratio))
    outfile.close()
    
    
