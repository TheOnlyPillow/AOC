class FileTreeNode:
    
    def __init__(self, type: str, name: str, size=0, ) -> None:
        self.name = name
        self.size = size
        self.type = type
        self.subfolders = []
        self.files = set()
        self.parent = None
        
    def __repr__(self) -> str:
        return(f"Folder: {self.name} Total Size: {self.size}")

    def has_subfolders(self):
        return len(self.subfolders) > 0
       
    def print_tree(self):
        if self.has_subfolders():
            for child_node in self.subfolders:
                child_node.print_tree()
        else:
            print(f"Folder: {self.name}, Size: {self.size}")
    
    def compute_tree_folder_sizes(self):
        total_size = 0
        if self.has_subfolders():
            for child_node in self.subfolders:
                total_size += child_node.compute_tree_folder_sizes()
        if len(self.files) > 0:
            for file in self.files:
                total_size += file.size
        self.size = total_size
        return total_size
    
    def total_of_folders_under_100k(self):
        total = 0
        if self.has_subfolders():
            for child_node in self.subfolders:
                total += child_node.total_of_folders_under_100k()
        if self.size <= 100000:
            total += self.size
        return total
     
def read_file():
    with open("2022\Day7\input.txt", "r", newline="\n") as file:
        return file.readlines()

def create_folder_node(line: str, current_node: FileTreeNode):
    folder_node = FileTreeNode("folder",line.split()[1])
    folder_node.parent = current_node
    current_node.subfolders.append(folder_node)
    return folder_node
    
def create_file_node(line: str, current_node: FileTreeNode):
    split_line = line.split()
    size = int(split_line[0])
    name = split_line[1]
    file_node = FileTreeNode("file",name,size)
    file_node.parent = current_node
    current_node.files.add(file_node)
    return file_node
                
def read_file_into_tree():
    node_stack = []
    folders = {}
    for line in read_file():
        line = line.rstrip()
        if "cd /" in line:
            root_node = FileTreeNode("folder","/")
            current_node = root_node
            
        elif "$ ls" in line:
            continue
        
        elif "dir " in line:
            folders[line.split()[1]] = line
            
        elif "$ cd" in line:
            if ".." in line:
                current_node = node_stack.pop()
                if folder_to_move_to:
                    if current_node != root_node:
                        folder_to_move_to = current_node.parent.name
                    else:
                        folder_to_move_to = root_node.name
                
            else:
                folder_to_move_to = line.split()[2]
                node_stack.append(current_node)
                current_node = create_folder_node(folders[folder_to_move_to], current_node)
        else:
            create_file_node(line, current_node)
    return root_node

def part1():
    root_node = read_file_into_tree()
    root_node.compute_tree_folder_sizes()
    # root_node.print_tree()
    return root_node.total_of_folders_under_100k()
    
if __name__ == "__main__":
    print(part1())