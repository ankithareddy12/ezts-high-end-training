class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
        for i in range(10):
            new_node = Node(i)
            if self.start is None:
                self.start = new_node
                temp = self.start
            else:
                temp.next = new_node
                temp = temp.next

# Helper function to print the linked list
def print_linked_list(linked_list):
    current = linked_list.start
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Create a linked list with values from 0 to 9
my_linked_list = LinkedList()

# Print the linked list
print("Linked list:")
print_linked_list(my_linked_list)
