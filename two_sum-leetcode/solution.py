class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        sorted_nums = sorted(nums)
        while i < j:
            print(sorted_nums[i] + sorted_nums[j])
            if sorted_nums[i] + sorted_nums[j] == target:
                return [i, j]
            elif sorted_nums[i] + sorted_nums[j] > target:
                j -= 1
            else:
                i += 1

if __name__ == '__main__':
    s = Solution()
    ip = [3, 2, 4]
    t = 6
    print(s.twoSum(ip, t))
