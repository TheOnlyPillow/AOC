all_stacks = {}

class Stack:
    
    def __init__(self):
        self.items = []
    
    def __repr__(self) -> str:
        return self.items.__str__()
    
    def push(self, item):
        if item == None:
            pass
        else:
            self.items.append(item)
            
    def multi_push(self, items):
        for item in items:
            self.push(item)
    
    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()
    
    def pop_multiple(self, num_to_pop):
        items = self.items[-1*(num_to_pop):]
        for index in range(num_to_pop):
            self.items.pop()
        return items
    
    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]
    

def check_if_in_stack(index):
    if index < 1:
        return 0
    elif index == 1:
        return 1
    elif index % 4 == 1:
        return int(round(index / 4 + 1,0))
    else:
        return 0

def create_stack(stack_number):
    if stack_number not in all_stacks.keys():
        all_stacks[stack_number] = Stack()

def add_item_to_stack(stack, item):
    if item == "\\n":
        pass
    else:
        current_stack = all_stacks[stack]
        current_stack.push(item)

def get_action_to_do(line):
    line_words = line.split()
    action = []
    for word in line_words:
        if word.isdigit():
            action.append(int(word))
    return action

with open(r"C:\Users\jwinicki\Documents\Python\AdventOfCode2022\Day5\input.txt","r") as input_file:
    all_lines = input_file.readlines()
    for line_number, line in enumerate(all_lines):
        if "[" in line:
            for index, character in enumerate(line):
                if character != "[" and character != "]" and character != " ":
                    stack_num = check_if_in_stack(index)
                    create_stack(stack_num)
                    add_item_to_stack(stack_num, character)
    del all_stacks[0] # Deletes a stack that's full of /n 
    for stack in all_stacks:
        all_stacks[stack].items.reverse() # reverses the stacks as values were entered backwards
    for line in all_lines:
        if "move" in line:
            action = get_action_to_do(line)
            num_items_to_move = action[0]
            src_stack_number = action[1]
            dest_stack_number = action[2]
            src_stack = all_stacks[src_stack_number]
            dest_stack = all_stacks[dest_stack_number]
            src_stack_items = src_stack.pop_multiple(num_items_to_move)
            dest_stack.multi_push(src_stack_items)

result_string = ""
for stack in (sorted(list(all_stacks.keys()))):
    result_string += all_stacks[stack].peek()
    
print(result_string)