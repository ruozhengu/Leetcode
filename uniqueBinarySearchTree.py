"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""
# G(n)=∑i=1n ​G(i−1)⋅G(n−i)
# run time O(n^2)
class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        
        for i in range(2, n+1):
            for j in range(1, i+1):
                
                dp[i] += dp[j-1] * dp[i-j]
                
        print(dp) 
        return dp[n]
        