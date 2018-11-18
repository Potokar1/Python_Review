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
        # We get the list head so we can step through the linked list
        current = self.head
        # At first our count for how many data elements in the llist is zero
        count = 0
        # keep going through the list until we reach the end (end is current == null)
        while current:
            # If the current node in the LList matches the given data specification
            if current.data == data:
                # Increase the count
                count += 1
            # Get the next node in the linked list
            current = current.next
        # Return count after we have reached the end of the linked list
        return count

    # This function will count the amount of occurances in a linked list
    def count_occurances_recursively(self, data):
        # Get the list head from the llist
        node = self.head
        # recursive helper method. Notice, takes node and data not self and data
        def _count_occurances_recursively(node,data):
            # Notice how this looks a lot like the iterative method. Not very 'recursive'
            count = 0
            if node and node.data == data:
                    count += 1
            if node.next:
                count += _count_occurances_recursively(node.next,data)
            return count
        # This is actually the first instance of using the helper method defined above
        return _count_occurances_recursively(node, data)

    # This is a more simple and elengent version of the recursive count function
    def count_occurances_recursively_simple(self,node,data):
        # Base case: if the node is null, ie we are at the end of the llist
        if not node:
            # Return zero because null !- data
            return 0
        # 'Yes Case' return 1 plus a call to the method with the next node from the llist
        if node.data == data:
            # Return 1 plus the amount returned by the call with the rest of the llist
            return 1 + self.count_occurances_recursively_simple(node.next, data)
        # 'No Case' only return call to the method with the next node from the llist
        else:
            # Return what is left in the list becuase the current node wasn't a match
            return self.count_occurances_recursively_simple(node.next, data)

    # We want to 'rotate' the list about the nth element.
    # so 1,2,3,4,5 -> rotate about 3rd element -> 4,5,1,2,3
    def rotate_list_about_nth(self,index):
        # Current will eventually hold the node that we rotate around
        current = self.head
        old_head = self.head
        # index -1 becuase we want the nth node not the next node after the nth
        for _ in range(index -1):
            current = current.next
        # Now current is the node we want at the end of our list.
        # The next node (or index plus one) will be the new list head
        new_head = current.next
        # Now we set the next node to null becuase this is the end to the new rotated llist
        current.next = None
        self.head = new_head
        # This is the last node from before we did a rotation
        # Now this will be the node right before the beginning of the list before rotation
        old_last = new_head
        # Now we want to get to the end of the list, so we can append the old end to the old beginning
        # .next because we don't want the null node we want the node before the null node
        while old_last.next:
            old_last = old_last.next
        # Now we have the last node in the llist, The next node is the null end node.
        # So we take the old list head and put the element up to the rotation node on the end
        old_last.next = old_head

    def is_palindrome(self):
        '''
        # Method 1: Using a string and the one liner for reverse strings
        s = ''
        # Pointer to the head of the list
        p = self.head
        # Store the list into a string
        while p:
            s += p.data
            p = p.next
        # Now s should contain the entire list in string form
        # This s[::-1] is the python one liner to check for palindromes (reverses list)
        return s == s[::-1]
        '''
        '''
        # Method 2: Using a list and the append and pop methods (like a stack)
        p = self.head
        # This is basically the stack we are using to reverse the list
        s = []
        # Store all the elements in the 'stack' so they will be popped in reveres order
        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        # This is where we compare each pop with the original list to see if it is palindrome
        while p:
            # Pop the top element off the stack, First iteration it is the last element
            data = s.pop()
            # If they are not the same, Then it is not a palindrome, exit by returning false
            if p.data != data:
                return False
            p = p.next
        # If we never return false, then we return true: is a palindrome
        return True
        '''
        # Method 3: two pointers (one for the head and one for the end,) + a prior pointer
        p = self.head
        q = self.head
        prior = []

        # A count so we can look at the individual nodes in the llist in reverse order
        i = 0
        # Get q to the last node in the llist
        while q:
            # append each node q to a list as we march along the llist
            prior.append(q)
            q = q.next
            i += 1
        # Set q back to the last element and not the null element at the end of llist
        q = prior[i-1]

        count = 1
        # We will only run this for i BASH 2 + 1 becuase we don't want to look at extra elements
        while count <= i//2 + 1:
            # This is how we can access the reverese of the list we just made
            # The last element is -1, then the second last is -2 and so on
            if prior[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True

    def move_tail_to_head(self):
        # p for the head pointer
        p = self.head
        # q for the tail pointer
        q = self.head
        prior = None
        # Get the tail pointer to point at the tail
        while q.next:
            prior = q
            q = q.next
        # The switcheroo
        q.next = p.next
        p.next = None
        prior.next = p
        self.head = q

    # We are going to be adding two llists together. Note that the least sig digit
    # is stored in the first entry, so the number is 'backwards' with how it's stored
    def sum_of_two(self,list2):
        # List head of the first llist
        p = self.head
        # List head of the second llist
        q = list2.head
        # Now we do addition, and we have to keep track of carry in's and outs
        carry_in = 0
        carry_out = 0
        temp_sum = 0
        sum = 0
        i = 0
        # first entry plus the second entry
        while p and q:
            carry_in = carry_out
            temp_sum = p.data + q.data + carry_in
            if temp_sum > 9:
                carry_out = 1
                temp_sum -= 10
            else:
                carry_out = 0
            sum += temp_sum * (10 ** i)
            i += 1
            p = p.next
            q = q.next
        # Now we have to account for the rest of the nodes, if any in either list
        while p:
            carry_in = carry_out
            temp_sum = p.data + carry_in
            if temp_sum > 9:
                carry_out = 1
                temp_sum -= 10
            else:
                carry_out = 0
            sum += temp_sum * (10 ** i)
            i += 1
            p = p.next
        while q:
            carry_in = carry_out
            temp_sum = q.data + carry_in
            if temp_sum > 9:
                carry_out = 1
                temp_sum -= 10
            else:
                carry_out = 0
            sum += temp_sum * (10 ** i)
            i += 1
            q = q.next
        return sum


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
'''
llist = LinkedList()
llist.append('A')
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
print(llist.count_occurances_iteratively('A'))
print(llist.count_occurances_recursively('A'))
print(llist.count_occurances_recursively_simple(llist.head,'A'))
'''
'''
llist = LinkedList()
llist.append('A')
llist.append('A')
llist.append('B')
llist.append('B')
llist.append('C')
llist.append('C')
llist.append('D')
llist.append('D')
llist.rotate_list_about_nth(3)
llist.print_list()
'''
'''
llist1 = LinkedList()
llist1.append('R')
llist1.append('A')
llist1.append('D')
llist1.append('A')
llist1.append('R')
llist2 = LinkedList()
llist2.append('A')
llist2.append('B')
llist2.append('C')
llist3 = LinkedList()
llist3.append('A')
llist3.append('N')
llist3.append('U')
llist3.append('T')
llist3.append('F')
llist3.append('O')
llist3.append('R')
llist3.append('A')
llist3.append('J')
llist3.append('A')
llist3.append('R')
llist3.append('O')
llist3.append('F')
llist3.append('T')
llist3.append('U')
llist3.append('N')
llist3.append('A')
print(llist1.is_palindrome())
print(llist2.is_palindrome())
print(llist3.is_palindrome())
'''
'''
llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.move_tail_to_head()
llist.print_list()
'''
'''
llist = LinkedList()
llist.append(9)
llist.append(9)
llist.append(9)
llist.append(9)
llist.append(9)
llist.append(1)
llist2 = LinkedList()
llist2.append(9)
llist2.append(9)
llist2.append(9)
print(llist.sum_of_two(llist2))
'''
