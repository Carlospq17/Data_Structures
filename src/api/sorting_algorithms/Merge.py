from api.sorting_algorithms.SortInterface import SortInterface

class Merge(SortInterface):

    def sort(self, arr):
        try:
            if len(arr) > 1:
                r = len(arr)//2
                L = arr[:r]
                M = arr[r:]

                self.sort(L)
                self.sort(M)

                i = j = k = 0

                while i < len(L) and j < len(M):
                    if L[i] < M[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = M[j]
                        j += 1
                    k += 1

                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1

                while j < len(M):
                    arr[k] = M[j]
                    j += 1
                    k += 1
        except:
            print("Something went really wrong")
            print("This should be a Log error message")
        finally:
            return arr