class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
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

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('Previous node is not in the list')
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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
