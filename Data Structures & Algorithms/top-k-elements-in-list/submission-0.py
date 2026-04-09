class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #create dict and count frequency of numbers
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        #create bucket
        buckets = [[] for _ in range(len(nums)+1)]

        # populate bucket
        for num in freq:
            buckets[freq[num]].append(num)

        #find top K
        res = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res