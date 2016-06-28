#!/usr/bin/python
#cycle.py

class Cycle:
	def __init__(self, c = []):
		self.elements = [x for x in c]
		self.f = 0
		self.size = len(self.elements)
		
	def front(self):
		return self.elements[self.f]
		
	def set_elements(self, el, fr = 0):
		self.elements = [x for x in el]
		self.f = fr
		self.size = len(self.elements)
		
	def init_front(self):
		self.f = 0
		
	def shift_cw(self):
		self.f = (self.f + 1) % self.size
		
	def shift_ccw(self):
		self.f = (self.f - 1) % self.size
		
	#positive shifts are clockwise, negative shifts are counter-clockwise.
	def shift_by(self, shift):
		self.f = (self.f + shift) % self.size
		
	#added in such a way that self.front() returns x.
	def add_at_front(self, x):
		self.elements = self.elements[:self.f] + [x] + self.elements[self.f:]
		self.size = len(self.elements)
	
	def add_at_back(self, x):
		self.add_at_front(x)
		self.shift_cw()
		
	#remove element at 'front' of list, new 'front' is next clockwise element.
	def pop_front(self):
		x = self.front()
		self.elements = self.elements[:self.f] + self.elements[self.f+1:]
		self.size = len(self.elements)
		self.f = self.f % self.size
		return x
		
	def __repr__(self):
		return self.__str__()
		
	def __str__(self):
		return str(self.elements[self.f:] + self.elements[:self.f])
		
	def __len__(self):
		return self.size
	
