class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # s = set(nums)
        # longest = 0

        # for n in nums:
        #     if (n-1) not in s:
        #         length = 0
        #         while(n+length) in s:
        #             length += 1
        #         longest = max(length, longest)
        # return longest

        #My own solution 1

        # if not nums :
        #     return 0

        # s = set(nums)
        # seq = {}

        # for n in nums:
        #     if n - 1 not in s:
        #         length = 0
        #         current = n

        #         while current in s:
        #             length += 1
        #             current += 1
        #         #stores seq length
        #         seq[n] = length

        # return max(seq.values())


        # better version of my own solution

        s = set(nums)
        longest = 0

        for i in nums:
            if i - 1 not in s:

                length = 0
                current = i

                while current in s:
                    length += 1
                    current += 1
                longest = max(length, longest)
        return longest
