import numpy as np

class InsertionSort(object):
    def insertionSort(self, array):
        """
        :type array: before sort
        :rtype: array: after sort
        """
        l = len(array)
        for i in range(1, l):
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] > key:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = key
        return array

if __name__ == '__main__':
    #
    array = np.random.rand(10)
    print array
    solution = InsertionSort()
    print solution.insertionSort(array)