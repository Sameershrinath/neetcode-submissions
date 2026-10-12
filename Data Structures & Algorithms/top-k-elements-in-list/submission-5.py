class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for i in range(k):
            maxi = max(freq.values())

            for j in freq:
                if freq[j] == maxi:
                    ans.append(j)
                    freq.pop(j)
                    break

        return ans