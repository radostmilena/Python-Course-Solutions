#!/usr/bin/python3

class Fish:
	def __init__(self):
		self.members = ['Shark', 'Fugu', 'Piranha']

	def printMembers(self):
		print('Printing members of the Fish class')
		for member in self.members:
			print('\t%s ' % member)
