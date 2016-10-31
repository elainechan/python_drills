'''
linked_list.py
'''

class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.list = []
        self.append()
        self.next_node = next_node

    def append(self):
        self.list.append(self.data)

    def new_head(self):
    	self.data = data

class LinkedList(list):
	
    def __init__(self, next_node):
        self.list = LinkedList()
        self.next_node = next_node

    def append(self, item):
        self.head = Node(item, next_node)

    def __len__(self):
        self.size = len()

    def __getitem__(self):
        pass

#    def pop(self):
#        pass
#
#    def __delitem__(self):
#        pass
