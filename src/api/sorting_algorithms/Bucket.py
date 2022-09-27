from api.sorting_algorithms.SortInterface import SortInterface

class Bucket(SortInterface):

	def func_insertion_sort(self, a):
		for i in range(1, len(a)):
			r = a[i]
			j = i - 1
			while j >= 0 and a[j] > r:
				a[j+1] = a[j]
				j -= 1
			a[j+1] = r
		return a

	def sort(self, arr):
		arr = []
		bucket_slot_num = 10
		
		try:
			for i in range(bucket_slot_num):
				arr.append([])
			for j in arr:
				index_b = int(bucket_slot_num * j)
				arr[index_b]
				arr[index_b].append(j)
			for i in range(bucket_slot_num):
				arr[i] = self.func_insertion_sort(arr[i])
			k = 0
			for i in range(bucket_slot_num):
				for j in range(len(arr[i])):
					arr[k] = arr[i][j]
					k += 1
		except:
			print("Something went really wrong")
			print("This should be a Log error message")
		finally:
			return arr