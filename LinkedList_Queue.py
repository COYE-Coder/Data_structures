#Linked List implementation of a FIFO Queue

class Node(object):
	def __init__(self,data):
		self.data = data
		self.next = None
		self.previous = None

class LinkedList(Node):

	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	#Appends to end of LL
	def append(self,new_node):
		current = self.head
		previous = None

		if current:
			while current.next:
				current = current.next
			current.next = new_node
			new_node.previous = current		
			self.tail = new_node

		else:
			self.head = new_node

	#Returns a node at a given position (first position is 0)
	def get_node(self,position):
		current = self.head
		pos = 0
		while current:
			if pos == position:
				return current
			pos += 1
			current = current.next
		return None


	#Inserts an element to LL
	def insert(self,new_node,position):
		behind_node = self.get_node(position-1)
		new_node.next = self.get_node(position)

		if behind_node:
			behind_node.next = new_node
			new_node.previous = behind_node
		else:
			self.head = new_node



	def get_f_position(self,data):
		current = self.head
		pos = 0

		while current:
			pos += 1
			if current.data == data:
				return pos
				
			current = current.next
		return None	


	def get_b_position(self,data):
		current = self.tail
		backPos = 0

		while current.previous:
			backPos += 1
			if current.data == data:
				return backPos

			current = current.previous
		return None


	#Deletes the last element with specific data
	def delete_last(self,data):
		bPos = get_b_position(data)
		
		if bPos:
			old_node = self.get_node(bPos)
			previous_node = self.get_node(bPos-1)
			previous_node.next = old_node.next
			previous_node.previous = old_node.previous


	def pop(self):
		old_last = self.tail
		new_last = old_last.previous
		new_last.next = None
		return old_last






class Queue(LinkedList):
	def __init__(self,ll):
		self.storage = ll

	def enqueue(self,new_element):
		self.storage.insert(new_element,0)

	def peek(self):
		return self.storage.get_node(0)

	def dequeue(self):
		return self.storage.pop()


	def printQueue(self):
		current = self.storage.head
		values = []

		while current.next:
			values.append(current.data)
			current = current.next

		print(values)


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



#Testing and troubleshooting    
q = Queue(ll)
q.enqueue(Node(2))
q.enqueue(Node(3))

# Test peek
# Should be 1
print (q.peek().data)

# Test dequeue
# Should be 1
print (q.dequeue().data)

# Test enqueue
q.enqueue(Node(4))
# Should be 2
print (q.dequeue().data)
# Should be 3
print (q.dequeue().data)
# Should be 4
print (q.dequeue().data)

q.enqueue(Node(5))
# Should be 5
print (q.peek().data)

q.printQueue()






