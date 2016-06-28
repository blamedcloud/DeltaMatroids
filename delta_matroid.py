#!/usr/bin/python
#delta_matroid.py

def sym_diff(s1,s2):
	result = []
	for x in s1:
		if x not in s2:
			if x not in result:
				result += [x]
	for x in s2:
		if x not in s1:
			if x not in result:
				result += [x]
	return result


class DeltaMatroid:
	def __init__(self, g = [], f = []):
		self.ground = g
		self.feasible = f
		
	def check_validity(self, quiet = False):
		if not quiet:
			print self.ground
			print self.feasible
		valid = True
		if (len(self.feasible) == 0) or (len(self.ground) == 0):
			if not quiet:
				print "Feasible sets or ground set is empty."
			valid = False
		if valid:
			for subset in self.feasible:
				if valid:
					for x in subset:
						if x not in self.ground:
							valid = False
							if not quiet:
								print "Feasible sets are not all subsets of the ground set."
							break
		if valid:
			check = False
			for f1 in self.feasible:
				for f2 in self.feasible:
					f3 = sym_diff(f1,f2)
					for x in f3:
						for y in f3:
							f4 = sym_diff(f1,[x,y])
							if f4 in self.feasible:
								check = True
								break
						if not check:
							valid = False
							if not quiet:
								print "Symmetric Exchange Axiom fails for:"
							print f1,f2
							break
					if not valid:
						break
				if not valid:
					break
		if not quiet:
			if valid:
				print "This is a delta-matroid!"
			else:
				print "This is not a delta-matroid."
		return valid
	
	def is_delta_matroid(self):
		return check_validity(self, True)
		
	#as of now, this function assumes self is a valid delta_matroid
	def is_matroid(self):
		valid = True
		if len(self.feasible) == 0:
			valid = False
		if valid:
			size = len(self.feasible[0])
			for f in self.feasible:
				if len(f) != size:
					valid = False
					break
		return valid
		
