#!/usr/bin/python3

class Mammals:
	def __init__(self):
		self.members = ['Tiger', 'Lion', 'Wild Cat']

	def printMembers(self):
		print('Printing members of the Mammals class')
		for member in self.members:
			print('\t%s ' % member)
