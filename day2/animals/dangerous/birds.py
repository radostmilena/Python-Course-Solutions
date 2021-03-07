#!/usr/bin/python3


class Birds:
	def __init__(self):
		self.members = ['Vulture', 'Eagle', 'Duck']

	def printMembers(self):
		print('Printing members of the Birds class')
		for member in self.members:
			print('\t%s ' % member)
