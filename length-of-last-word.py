# https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split()
        # We're getting the length of the last item of the word list (index denoted as len(word_list) - 1).
        return len(word_list[len(word_list) - 1])
print(Solution.lengthOfLastWord(None, "Hello World"))
print(Solution.lengthOfLastWord(None, "   fly me   to   the moon  "))
print(Solution.lengthOfLastWord(None, "luffy is still joyboy"))