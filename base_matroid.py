#!/usr/bin/python
#base_matroid.py

def is_proper_subset(small, big):
	result = True
	if len(big) > len(small):
		for x in small:
			if x not in big:
				result = False
	else:
		result = False
	return result
	
def less(s1, s2):
	result = []
	for x in s1:
		if x not in s2:
			result += [x]
	return result

class BaseMatroid:
	def __init__(self, g = [], b = [])
		self.ground = g
		self.bases = b
		
	def check_validity(self, quiet = False):
		valid = True
		if (len(self.bases) == 0) or (len(self.ground) == 0):
			if not quiet:
				print "Bases or ground set is empty."
			valid = False
		if valid:
			for b1 in self.bases:
				for b2 in self.bases:
					if is_proper_subset(b1,b2):
						valid = False
						break
				if not valid:
					break
		if valid:
			check = False
			for B1 in self.bases:
				for B2 in self.bases:
					for b1 in less(B1,B2):
						for b2 in less(B2,B1):
							if (less(B1,[b1]) + [b2]) in self.bases:
								check = True
								break
						if not check:
							valid = False
							break
					if not valid:
						break
				if not valid:
					break
		return valid
							
