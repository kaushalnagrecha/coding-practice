class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m = len(nums1)
        n = len(nums2)

        # Ensure nums1 is the shorter array
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        # Initialize the search range
        low = 0
        high = m

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX

            maxLeftX = nums1[partitionX - 1] if partitionX > 0 else float("-inf")
            minRightX = nums1[partitionX] if partitionX < m else float("inf")
            maxLeftY = nums2[partitionY - 1] if partitionY > 0 else float("-inf")
            minRightY = nums2[partitionY] if partitionY < n else float("inf")

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1

        return -1
            
if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,3],[2]))