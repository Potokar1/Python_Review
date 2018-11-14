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
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    # Swap two nodes with given key_1 and key_2
    def swap_nodes(self, key_1, key_2):
        # Check to see if the two nodes to swap are the same node
        if key_1 == key_2:
            return

        prev_node1 = None
        cur_node1 = self.head
        # Get the node with the data = key_1. after iteration cur_node1 is first node to be swapped.
        while cur_node1 and cur_node1.data != key_1:
            prev_node1 = cur_node1
            cur_node1 = cur_node1.next

        prev_node2 = None
        cur_node2 = self.head
        # Get the node with the data = key_2. after iteration cur_node1 is second node to be swapped.
        while cur_node2 and cur_node2.data != key_2:
            prev_node2 = cur_node2
            cur_node2 = cur_node2.next

        # Check to see if either of these are None which would mean that element is not in the list.
        if not cur_node1 or not cur_node2:
            return

        # Check to see if key_1's node is Not the list head
        if prev_node1:
            prev_node1.next = cur_node2
        # It is the list head
        else:
            self.head = cur_node2
        # Check to see if key_2's node is Not the list head
        if prev_node2:
            prev_node2.next = cur_node1
        # It is the list head
        else:
            self.head = cur_node1

        # Swap the two node's next pointers to complete the swap
        cur_node1.next, cur_node2.next = cur_node2.next, cur_node1.next

    # Used to keep track of what node is being worked during an iterative process.
    # Name is the type of node we are looking at. Can be current node or previous, ect..
    def print_helper(self, node, name):
        if node is None:
            print(name + ': None')
        else:
            print(name + ':' + node.data)

    # Visualiztion of what we are trying to do reversing list
    # A -> B -> C -> D -> 0
    # D -> C -> B -> A -> 0
    # A <- B <- C <- D <- 0

    # Reverse a given list iteratively
    def reverse_iterative(self):
        prior = None
        current = self.head
        while current:
            next = current.next
            current.next = prior
            ''' This is to help see which nodes are being worked each iteration
            self.print_helper(prior, 'Prior Node')
            self.print_helper(current, 'Current Node')
            self.print_helper(next, 'Next node')
            print()
            '''
            prior = current
            current = next
        self.head = prior

    # Reverse a given list recursively
    # Here we don't call the acutal function but the recursive helper function recursively
    def reverse_recursive(self):

        # A recursive helper function, used like the while loop of iterative implementaion
        def _reverse_recursive(current, prior):
            if not current:
                return prior
            next = current.next
            current.next = prior
            ''' This is to help see which nodes are being worked each iteration
            self.print_helper(prior, 'Prior Node')
            self.print_helper(current, 'Current Node')
            self.print_helper(next, 'Next node')
            print()
            '''
            prior = current
            current = next
            # Here we do the recursive call to march down the llist and reverse the pointers
            return _reverse_recursive(current, prior)

        # Very similar to self.head = prior in iterative implementaion
        self.head = _reverse_recursive(current=self.head, prior=None)

    # This function will combine the first_list.merge_lists(second_list)
    # Requires that the lists are already sorted
    # Returns a new sorted list, a combination of the two input lists.
    def merge_sorted(self, list2):
        list1_current = self.head
        list2_current = list2.head
        merged_llist = LinkedList()
        # We will go over the elements in each list and put them into a new array
        # We will be making n comparisons where n is # of all elements in both lists
        for index in range(self.len_iterative() + list2.len_iterative()):
            ''' This is to help keep track of each comparsion each iteration
            self.print_helper(list1_current, 'list1_current')
            list2.print_helper(list2_current, 'list2_current')
            print()
            '''
            # If both linked lists still have elements
            if list1_current and list2_current:
                # If the first list's element is before the second's, append the first's
                if list1_current.data < list2_current.data:
                    merged_llist.append(list1_current.data)
                    list1_current = list1_current.next
                # Otherwise append the second's to the merged linked list
                else:
                    merged_llist.append(list2_current.data)
                    list2_current = list2_current.next
            # If one of the lists is empty before we are done (size missmatch)
            else:
                # If there are elements left in the first list, append the rest
                if list1_current:
                    merged_llist.append(list1_current.data)
                    list1_current = list1_current.next
                # If there are elements left in the second list, append the rest
                else:
                    merged_llist.append(list2_current.data)
                    list2_current = list2_current.next
        # return the merged linked list
        return merged_llist

    # This function removes the duplicates in a given lists.
    # Keeps the first element, deletes repeats
    def remove_duplicates(self):
        current = self.head
        to_be_removed = []
        prior = None
        # Keep track of the values we have already seen
        seen = []
        # So we know which node to delete from the linked list
        position = 0
        # While we still have elements
        while current:
            # If the current node's data is not in seen
            if current.data not in seen:
                # add that data to the list so we know we've seen it
                to_be_removed.append(current.data)
            # If the current node's data has been seen before, so duplicate
            else:
                # Delete that node at that position
                self.delete_node_at_position(position)
                # We deleted the current node so we will take a step back
                current = prior
                # We lost an element in the linked list so this adjusts for that
                position -= 1
            # march through the linked list and increase the position of which node we are on.
            prior = current
            current = current.next
            position += 1

    # This fuction will return the nth to last node in the linke list
    # Example: n = 1 is  the last, n = 2 will give the second (to) last element, and so on
    def nth_to_last(self, n):
        # If we get a postiion that is not in the list we want to send an error message
        if self.len_iterative() - n < 0:
            print('ERROR, need to give a node within the size of {}'.format(self.len_iterative()))
            return
        # We have proper input
        else:
            current = self.head
            # We go through the list until we get to the element we want to return
            for _ in range(self.len_iterative() - n):
                current = current.next
            return current.data

    # This function will count the amount of occurances in a linked list
    def count_occurances_iteratively(self, data):
        pass

    # This function will count the amount of occurances in a linked list
    def count_occurances_recursively(self, data):
        pass


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
print()
llist.print_list()
print()
llist.swap_nodes('A', 'B')
llist.print_list()
print()
llist.swap_nodes('C', 'B')
llist.print_list()
print()
llist.swap_nodes('B', 'A')
llist.print_list()
print()
llist.swap_nodes('A', 'C')
llist.print_list()
print()
llist.append('D')
llist.print_list()
print()
llist.reverse_iterative()
llist.print_list()
print()
llist.reverse_iterative()
llist.print_list()
print()
llist.reverse_recursive()
llist.print_list()
print()
llist.reverse_recursive()
llist.print_list()
print()


#initialize two linked lists to be merged
first = LinkedList()
first.append('a')
first.append('c')
first.append('e')
first.append('g')
first.print_list()
print()
second = LinkedList()
second.append('b')
second.append('d')
second.append('f')
second.append('h')
second.append('i')
second.print_list()
print()
merged_list = first.merge_sorted(second)
print()
merged_list.print_list()

#initialize two linked lists to be merged
first = LinkedList()
first.print_list()
print()
second = LinkedList()
second.append('b')
second.append('d')
second.append('f')
second.append('h')
second.append('i')
second.print_list()
print()
merged_list = first.merge_sorted(second)
print()
merged_list.print_list()


duplicates = LinkedList()
duplicates.append('A')
duplicates.append('A')
duplicates.append('C')
duplicates.append('B')
duplicates.append('C')
duplicates.append('B')
duplicates.append('D')
duplicates.append('A')
duplicates.append('C')
duplicates.print_list()
print()
duplicates.remove_duplicates()
duplicates.print_list()
print()


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
print(llist.nth_to_last(4))
'''
