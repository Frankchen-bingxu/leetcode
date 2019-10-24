class Node(object):
	"""docstring for Node"""
	def __init__(self, data):
		self.data = data
		self.next = None

	def __str__(self):
		return str(self.data)
		
class LinkList(object):
	def __init__(self):
		self.head = None
		self.tail = None
	
	def is_empty(self):
		return self.head is None

	def append(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	def iter(self):
		if not self.head:
			return
		cur = self.head
		yield cur.data
		while cur.next:
			cur = cur.next
			yield cur.data

	def insert(self,idx,value):
		cur = self.head
		cur_idx = 0
		if cur is  None:
			raise Exception('This list is an is an empty list')
		while cur_idx < idx - 1:
			cur = cur.next
			if cur is None:
				raise Exception('list length less than index')
			cur_idx += 1
		node = None(value)
		node.next = cur.next
		cur.next = node
		if node.next is None:
			self.tail = node


	def remove(self,idx):
		cur = self.head
		cur_idx = 0
		if cur is None: #空链表时
			raise Exception("The list is an empty list")
		while cur_idx < idx - 1:
			cur = cur.next
			if cur is None:
				raise Exception("The list length is less than idx")
			cur_idx += 1
		#现在的cur是要删除节点的上一个节点
		if idx == 0:
			self.head = cur.next
			cur = cur.next
			return
		if self.head == self.tail:
			self.head = None
			self.tail = None
			return
		cur.next = cur.next.next
		if cur.next is None:
			self.tail = cur

	def size(self):
		cur = self.head
		count = 0
		if cur is None:
			raise Exception("This list is an empty list")
		while cur:
			cur = cur.next
			count += 1
		return count


	def search(self,item):
		cur = self.head
		found = False
		while cur is not None and not found:
			if cur.data == item:
				found = True
			else:
				cur = cur.next
		return found
			


if __name__ == '__main__':
	linklist = LinkList()
	for i in range(150):
		linklist.append(i)

	for node in linklist.iter():
		 print('node is {0}'.format(node))

	print(linklist.size())

