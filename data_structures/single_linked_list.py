
class LinkedList:
    # Initializes an empty linked list. null value == None
    def __init__(self):
        self.head = None

    # Print out every element of the list
    def print_list(self):
        cur_node = self.head
        # Continue to iterate through the list until cur_node is false (i.e. cur_node is not None )
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    # Insert in the last position 'append' does this always
    def append(self, data):
        new_node = Node(data)

        # List is empty so we want new node to be list head
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        # How to traverse through the list
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Insert in the first position (list_head)
    def preped(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert in the position directly after a given node.
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('Previous node is not in the list')
            return

        # Create the new node to be inserted
        new_node = Node(data)
        # Set the pointers up correctly
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Delete a node based on a given key, iterates through the linked list to find the node to delete
    def delete_node(self, key):

        # Start at the list head
        cur_node = self.head

        # Check if out furst node is the given key
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        # Iterate until at end of list or if we find the node with given key
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        # If we never found a node with the given key
        if cur_node is None:
            return

        # We found the node with the given key and now we delete that node
        # First we move pointers and then we put out toys away
        prev.next = cur_node.next
        cur_node = None

    # Delete a node at a given position.
    def delete_node_at_position(self, position):
        cur_node = self.head
        if position == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        i = 0
        # Traversing through the list
        while cur_node and i != position:
            prev = cur_node
            cur_node = cur_node.next
            i += 1

        # The node is never found and we get to end of list
        if cur_node is None:
            print()
            print('ERROR: POSITION NOT IN LIST')
            return

        # Delete
        prev.next = cur_node.next
        cur_node = None

    # Return the length of a given linked list. Done iteratevely
    def len_iterative(self):
        cur_node = self.head
        length = 0
        # Iterate while the current node isn't null
        while cur_node:
            cur_node = cur_node.next
            length += 1
        return length

    # Return the length of a given linked list. Done recursively
    def len_recursive(self,node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self,key_1,key_2):
        # Check to see if the two nodes to swap are the same node
        if key_1 == key_2:
            return
        cur_node = self.head
        # Check to see if the list head is a node to be swapped
        if cur_node.data == key_1 or cur_node.data == key_2:




# The Node. Linked lists are made of nodes with a data field and a next field.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
llist = LinkedList()
llist.append('A')
llist.append('B')
llist.print_list()
print()
llist.preped('C')
llist.print_list()
llist.insert_after_node(llist.head.next, 'E')
print()
print(llist.head.data)
print()
llist.print_list()
print()
llist.delete_node('E')
llist.print_list()
llist.delete_node('C')
print()
llist.print_list()
llist.append('C')
llist.append('D')
print()
llist.print_list()
llist.delete_node_at_position(3)
print()
llist.print_list()
print()
print(llist.len_iterative())
print()
print(llist.len_recursive(llist.head))
'''
