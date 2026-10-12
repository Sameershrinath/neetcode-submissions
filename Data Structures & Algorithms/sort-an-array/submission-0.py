class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.sortArray(arr[:mid])
        right = self.sortArray(arr[mid:])

        result = []
        i = 0
        j = 0

        # Merge the two sorted halves
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Append remaining elements
        result.extend(left[i:])
        result.extend(right[j:])

        return result
            