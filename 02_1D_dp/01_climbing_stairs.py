"""70. Climbing Stairs
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps"""
class Solution(object):
    def climbStairs(self, n):
        store={}
        """memoaisation"""
        def res(n):
            if n==1:return 1
            if n==2:return 2
            if n in store:
                return store[n]
            store[n]=res(n-1)+res(n-2)
            return store[n]
        return res(n)
            
        """
        :type n: int
        :rtype: int
        """
        