#!/usr/bin/python3

class Mammals:
	def __init__(self):
		self.members = ['Giraffe', 'Elephant', 'Zebra']

	def printMembers(self):
		print('Printing members of the Mammals class')
		for member in self.members:
			print('\t%s ' % member)
