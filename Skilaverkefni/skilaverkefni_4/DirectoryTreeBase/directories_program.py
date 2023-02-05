
class TreeNode:
    def __init__(self, name = "", back = None):
        self.name = name
        self.content = []
        self.back = back

'''
Note that all the "if False" and "if True" are simply there to
give you the correct success and error message formats.
You can use if sentences or try catch or any other
means of programming you control flow.
You can make an encapsulting class for everything and start with that,
rather than starting with the single TreeNode("root").
Just make sure the input and output of the program is exactly as
specified and fits with the  expected_out.txt when the tester
program is run with the original commands.txt.
Then feel free to make your own, more extensive tests.
'''

def get_names(tree):
    dir_names = []
    for node in tree.content:
        dir_names.append(node.name)
    return dir_names

def get_pos(tree, directory):
    pos = 0
    for node in tree.content:
        if node.name == directory:
            return pos
        pos += 1


def run_commands_on_tree(tree):
    print("  current directory: " + tree.name)
    while True:
        user_input = input()
        command = user_input.split()
        if command[0] == "mkdir":
            print("  Making subdirectory " + command[1])
            dir_names = get_names(tree)
            if command[1] in dir_names:
                print("  Subdirectory with same name already in directory")
            else:
                new_node = TreeNode(command[1], tree)
                tree.content.append(new_node)

        elif command[0] == "ls":
            print("  Listing the contents of current directory,  " + tree.name) # Add the name of the directory here
            dir_names = get_names(tree)
            for name in sorted(dir_names):
                print(name)

        elif command[0] == "cd":
            print("  switching to directory " + command[1])
                # command[1] is the name of the subdirectory that should now become the current directory
            if command[1] == "..":
                if tree.back == None:
                    print("Exiting directory program")
                    break
                else:
                    tree = tree.back
            else:
                dir_names = get_names(tree)
                if command[1] in dir_names:
                    pos = get_pos(tree, command[1])
                    tree = tree.content[pos]
                else:
                    print("  No folder with that name exists")
            print("  current directory: " + tree.name) # Add the name of the current directory here

        elif command[0] == "rm":
            print("  removing directory " + command[1])
                # command[1] is the name of the subdirectory that should now become the current directory
            dir_names = get_names(tree)
            if command[1] in dir_names:
                pos = get_pos(tree, command[1])
                directory = tree.content[pos]
                tree.content.remove(directory)
                print("  directory successfully removed!")
            else:
                print("  No folder with that name exists")
        else:
            print("  command not recognized")


def run_directories_program():
    # YOU CAN CHANGE THE WHOLE THING IF YOU LIKE!!
    # YOU CAN DESIGN THIS DIFFERENTLY IF IT SUITS YOU
    run_commands_on_tree(TreeNode("root"))

if __name__ == "__main__":
    run_directories_program()
    
