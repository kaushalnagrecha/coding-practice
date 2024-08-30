## Two Sum | Leetcode
Easy 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Examples - 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

### Constraints:
1. 2 <= nums.length <= 104
2. -109 <= nums[i] <= 109
3. -109 <= target <= 109
4. Only one valid answer exists.

### Approach - 
#### Theory - 
##### Simple Approach - 
1. Add each element of the input array with the other and check whether the sum matches or not
> T.C = O(N<sup>2</sup>) | S.C = O(1)
##### Smart Approach - 
1. Take the compliment of each element in the input array and check whether the compliment exists in the input array and return it's index!
> T.C = O(N) | S.C = O(N)
#### Algorithm - 
1. Initialize an empty dictionary/map - this map will contain values as key and indexs as value
2. for each element check if the compliment of the element already exists in the map
    1. if so return both the indexes
    2. if not add the number, index pair to the dictionary/ map
