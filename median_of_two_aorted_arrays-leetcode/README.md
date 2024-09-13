## Median of Two Sorted Arrays
Hard | LeetCode

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

### Examples:

Example 1 -
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2 -
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

### Constraints:
1. nums1.length == m
2. nums2.length == n
3. 0 <= m <= 1000
4. 0 <= n <= 1000
5. 1 <= m + n <= 2000
6. -106 <= nums1[i], nums2[i] <= 106

### Solution:
#### Approach - 
The key idea is to partition the two arrays into two parts such that the number of elements in the left part of both arrays is equal. Then, the median will be the average of the maximum element in the left part and the minimum element in the right part.

#### Steps - 
1. Ensure the shorter array is on the left. This will help in reducing the search space.
2. Set the search range for the partition index in the shorter array to be from 0 to its length.
3. Perform binary search:
    * Calculate the partition index for the longer array based on the partition index in the shorter array.
    * Find the maximum element in the left part of the shorter array.
    * Find the minimum element in the right part of the longer array.
    * If the maximum element in the left part of the shorter array is less than or equal to the minimum element in the right part of the longer array, the median is found.
    * Otherwise, adjust the search range based on the comparison and repeat the process.
