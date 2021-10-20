class SortArrayForSmallest():

    def findSmallest(self, arr):
        """
        O(n)
        """
        smallest = arr[0]
        smallest_index = 0

        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        return smallest_index

    def selectionSort(self, arr):
        """
        O(n*n) => O(n2)
        """
        newArr = []
        for _ in range(len(arr)):
            smallest = self.findSmallest(arr)
            newArr.append(arr.pop(smallest))
        return newArr
        
if __name__ == '__main__':
    sa = SortArrayForSmallest()
    arr = [1,8,0,3,9]
    print(sa.selectionSort(arr))