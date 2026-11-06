class Solution:
    def mergeTwoSortedArrays(self, left, right):
        i = j = k = 0
        mergedArray = [0] * (len(left) + len(right))

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                mergedArray[k] = left[i]
                i += 1
            else:
                mergedArray[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            mergedArray[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            mergedArray[k] = right[j]
            j += 1
            k += 1

        return mergedArray

    def mergeSort(self, nums, start, end):
        if start == end:
            return [nums[start]]

        mid = start + (end - start) // 2
        left = self.mergeSort(nums, start, mid)
        right = self.mergeSort(nums, mid + 1, end)

        return self.mergeTwoSortedArrays(left, right)

    def sortArray(self, nums):
        return self.mergeSort(nums, 0, len(nums) - 1)