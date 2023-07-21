from bisect import bisect_left
class Solution(object):
    def findNumberOfLIS(self, nums):
        dp = []
        num_sequences_of_length = collections.defaultdict(list)
        for i in range(len(nums)):
            pos = bisect_left(dp, nums[i])
            if pos == len(dp):
                dp.append(nums[i])
            else:
                dp[pos] = nums[i]
            total = 0
            for count, last in num_sequences_of_length[pos]:
                if last < nums[i]:
                    total += count
            num_sequences_of_length[pos+1].append((max(1, total), nums[i]))
        return sum([count for count,_ in num_sequences_of_length[len(dp)-1]])
