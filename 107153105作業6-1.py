class CircularQueue(): 

	# constructor 
	def __init__(self, size): # initializing the class 
		self.size = size 
		
		# initializing queue with none 
		self.queue = [None for i in range(size)] 
		self.head = self.tail = -1

	def set(self, data): 
		
		# condition if queue is full 
		if ((self.tail + 1) % self.size == self.head): 
			print(" Queue is Full\n") 
			
		# condition for empty queue 
		elif (self.head == -1): 
			self.head = 0
			self.tail = 0
			self.queue[self.tail] = data 
		else: 
			
			# next position of rear 
			self.tail = (self.tail + 1) % self.size 
			self.queue[self.tail] = data 
			
	def get(self): 
		if (self.head == -1): # codition for empty queue 
			print ("Queue is Empty\n") 
			
		# condition for only one element 
		elif (self.head == self.tail): 
			temp=self.queue[self.head] 
			self.head = -1
			self.tail = -1
			return temp 
		else: 
			temp = self.queue[self.head] 
			self.head = (self.head + 1) % self.size 
			return temp 

	def display(self): 
	
		# condition for empty queue 
		if(self.head == -1): 
			print ("Queue is Empty") 

		elif (self.tail >= self.head): 
			print("Elements in the circular queue are:", 
											end = " ") 
			for i in range(self.head, self.tail + 1): 
				print(self.queue[i], end = " ") 
			print () 

		else: 
			print ("Elements in Circular Queue are:", 
										end = " ") 
			for i in range(self.head, self.size): 
				print(self.queue[i], end = " ") 
			for i in range(0, self.tail + 1): 
				print(self.queue[i], end = " ") 
			print () 

		if ((self.tail + 1) % self.size == self.head): 
			print("Queue is Full") 

# Driver Code 
ob = CircularQueue(5) 
ob.set(14) 
ob.set(22) 
ob.set(13) 
ob.set(-6) 
ob.display() 
print ("Deleted value = ", ob.get()) 
print ("Deleted value = ", ob.get()) 
ob.display() 
ob.set(9) 
ob.set(20) 
ob.set(5) 
ob.display() 

# This code is contributed by AshwinGoel 
