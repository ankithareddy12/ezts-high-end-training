class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next  # Store the next node temporarily
        current.next = prev  # Reverse the direction

        # Move the pointers one step forward
        prev = current
        current = next_node

    # The new head is the previous tail node
    head = prev
    return head

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Original linked list:")
print_linked_list(head)

# Reverse the linked list
head = reverse_linked_list(head)

print("Reversed linked list:")
print_linked_list(head)
