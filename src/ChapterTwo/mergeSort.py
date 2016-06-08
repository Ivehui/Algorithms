import numpy as np

class MergeSort(object):
    def mergeSort(self, array, left, right):
        """
        :type array: before sort
        :rtype: array: after sort
        """
        if left < right:
            middle = (right + left) / 2
            self.mergeSort(array, left, middle)
            self.mergeSort(array, middle+1, right)
            self.merge(array, left, middle, right)
        return array

    def merge(self, array, left, middle, right):
        l1 = middle - left + 1
        l2 = right - middle
        a1 = np.zeros((l1+1,))
        a2 = np.zeros((l2+1,))
        for i in range(l1):
            a1[i] = array[left + i]
        for i in range(l2):
            a2[i] = array[middle + i + 1]
        a1[-1] = float("inf")
        a2[-1] = float("inf")
        i1 = 0
        i2 = 0
        for j in range(left, right+1):
            if a1[i1] < a2[i2]:
                array[j] = a1[i1]
                i1 += 1
            else:
                array[j] = a2[i2]
                i2 += 1
        return array

if __name__ == '__main__':
    #
    length = 5
    array = np.random.rand(length)
    print array
    solution = MergeSort()
    print solution.mergeSort(array, 0, length-1)
