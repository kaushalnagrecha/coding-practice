### Add Two Numbers
Medium | LeetCode

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#### Examples:

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

#### Constraints:
1. The number of nodes in each linked list is in the range [1, 100].
2. 0 <= Node.val <= 9
3. It is guaranteed that the list represents a number that does not have leading zeros.

#### Solution:
##### Approach - 
1. While both linked lists are not empty, add the corresponding nodes' values and the carry.
2. Create a new node with the sum % 10 as its value and set head.next to this new node.
3. Update the carry by dividing the sum by 10.
4. Move to the next nodes in both linked lists.
5. Handle remaining elements: 
    1. If one of the linked lists is not empty, continue adding its remaining values to the sum, considering the carry.
6. Handle final carry: 
    1. If there's a remaining carry, create a new node with the carry value and set head.next to it.
7. Return the result: 
    Return the next node of head, as head was a dummy node.
> T.C = O(N) | S.C = O(1)
