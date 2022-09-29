from api.sorting_algorithms.SortInterface import SortInterface
from random import random

class Bucket(SortInterface):

	def insertionSort(self, b):
		for i in range(1, len(b)):
			up = b[i]
			j = i - 1
			while j >= 0 and b[j] > up: 
				b[j + 1] = b[j]
				j -= 1
			b[j + 1] = up     
		return b     
				
	def sort(self, x):
		arr = []
		slot_num = 10

		for i in range(slot_num):
			arr.append([])
			
		for j in x:
			index_b = int(slot_num * j) 
			arr[index_b].append(j)
		
		for i in range(slot_num):
			arr[i] = self.insertionSort(arr[i])
			
		k = 0
		for i in range(slot_num):
			for j in range(len(arr[i])):
				x[k] = arr[i][j]
				k += 1
		return x

	def generateExampleArray(self, size):
		arr = []
		for _ in range(size):
			arr.append(round(random(), 3))
		return arr