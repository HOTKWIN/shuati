'''
Given a string,find the length of the longest substring without repeating characters.

Example 1:
Input:"abcabcbb"
Output:"3"
Explanation:The answer is 'abc',with the length of 3.

Example 2:
Input:"bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input:"pwwkew"
Output:3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
import collections

class Solution:
    def lengthOfLongestSubstring1(self,s):
        if not s or len(s) == 0:
            return 0

        l,r = 0,0
        res,lookup = 0,set()
        while l<len(s) and r<len(s):
            if s[r] not in lookup:
                lookup.add(s[r])
                res = max(res,r-l+1)
                r += 1
            else:
                lookup.discard(s[l])
                l += 1
        return res

    def lengthOfLongestSubstring2(self,s):
        start,res,maps,n = 0,0,{},len(s)
        for i in range(n):
            start = max(start,maps.get(s[i],-1)+1)
            res = max(res,i - start + 1)
            maps[s[i]] = i
        return res

    def lengthOfLongestSubstring3(self,s):
        lookup = collections.defaultdict(int)
        l,r,counter,res = 0,0,0,0
        while r<len(s):
            lookup[s[r]] += 1
            if lookup[s[r]] == 1:
                counter += 1
            r += 1
            #counter<r-l means repeat,counter==r-l means no repeat
            while l<r and counter<r-l:
                lookup[s[l]] -= 1
                if lookup[s[l]] == 0:
                    counter -= 1
                l += 1
            res = max(res,counter)
        return res

x = Solution()
print(x.lengthOfLongestSubstring3("pwwkew"))
