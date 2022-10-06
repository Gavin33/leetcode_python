class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        # keeps track of what substring we're on
        sub = ''
        max_index = len(s)
        # go through the letters one by one.
        for c in range(max_index):
            # Search substring for c
            char_index = sub.find(s[c])
            if char_index == -1:
                sub += s[c]
                if c != max_index - 1:
                    continue
            # Check if substring is > answer, replace if so
            final_sub = len(sub)
            if final_sub > ans:
                ans = final_sub
            # If duplicate, get rid of all characters before and including s[c] from sub, concat s[c]
            if char_index != -1:
                sub = sub[char_index + 1:] + s[c]
        return ans


print(Solution.lengthOfLongestSubstring(None, 'abcabcbb'))
print(Solution.lengthOfLongestSubstring(None, 'bbbbb'))
print(Solution.lengthOfLongestSubstring(None, 'pwwkew'))
print(Solution.lengthOfLongestSubstring(None, ' a '))
