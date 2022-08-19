class Node:
    """Storing a single node of a linked list"""
    data = None
    """Link to next node"""
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """Singly linked lists"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """Returns the number of elements in the linked list takes linear time"""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node

        return count

    def searched_val(self, val):
        """Search and return a node in the linked list that matches the given key"""
        current = self.head
        while current:
            if current.data == val:
                return current
            else:
                current = current.next_node
        return None

    def add(self, data):
        """Add a new node containing data at the head of the node"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def remove(self, data):
        """Remove an element/node that contain the data from the linked list"""
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == data and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == data:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def insert_at_index(self, data, index):
        """Insert a new node at a particular position in the linked list"""
        if index == 0:
            self.add(data)
        if index > 0:
            current = self.head
            new_node = Node(data)
            position = index

            while position > 1:
                current = current.next_node
                position -= 1
            previous_node = current
            next_node = current.next_node
            previous_node.next_node = new_node
            new_node.next_node = next_node

    def __repr__(self):
        """Returns a string representation of the linked list."""
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '->'.join(nodes)


L = LinkedList()
L.add(1)
L.add(2)
L.add(3)
print(L)
n = L.searched_val(3)
print(n)
L.insert_at_index(10, 2)
print(L)
L.insert_at_index(10, 3)
L.insert_at_index(10, 2)
print(L)
L.insert_at_index(15, 2)
print(L)
print(L.remove(2))
print(L)
