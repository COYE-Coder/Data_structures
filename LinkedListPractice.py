#First data structure exercise
# Quick implementation of Linked Lists


class Node(object):
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList(Node):
	def __init__(self,head=None):
		self.head = head

	def append(self,new_node):
		current = self.head
		if self.head:
			while current.next:
				current = current.next
			current.next = new_node
		else:
			self.head = new_element

	def get_node(self,position):
		pos = 1
		current = self.head

		while current:
			if pos == position:
				return current
			pos += 1
			current = current.next
		return None


	def insert(self,new_node,position):
		prevNode = self.get_node(position-1)
		new_node.next = self.get_node(position)
		prevNode.next = new_node

	def find(self,data):
		current = self.head
		pos = 0

		while current:
			pos += 1
			if current.data == data:
				return pos
				
			current = current.next
		return None	


	def delete(self,data):
		position = self.find(data)

		if position:
			old_node = self.get_node(position)
			previous = self.get_node(position-1)
			previous.next = old_node.next




#Testing and troubleshooting:

#Create 5 nodes
e1 = Node(15)
e2 = Node(16)
e3 = Node(10)
e4 = Node(11)
e5 = Node(20)

#Create Linked list
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)

#Should print e3's data (10)
print(ll.get_node(3).data)


#Insert new node at 5
i1 = Node(5)
ll.insert(i1,3)

#Should print i1's data (5)
print(ll.get_node(3).data)


#Should print 6
print(ll.find(20))

#Should print None
ll.delete(10)
print(ll.find(10))



